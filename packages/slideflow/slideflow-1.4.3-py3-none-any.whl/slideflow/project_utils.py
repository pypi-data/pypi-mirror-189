"""Utility functions for slideflow.Project."""

import logging
import os
from collections import defaultdict
from functools import wraps
from os.path import dirname, exists, join, realpath
from types import SimpleNamespace
from typing import Any, Callable, Dict, List, Optional, Tuple, Union

import slideflow as sf
from slideflow import errors
from slideflow.util import log, relative_path

# Set the tensorflow logger
if sf.getLoggingLevel() == logging.DEBUG:
    logging.getLogger('tensorflow').setLevel(logging.DEBUG)
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '0'
else:
    logging.getLogger('tensorflow').setLevel(logging.ERROR)
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'


def auto_dataset(method: Callable):
    """Wrapper to convert filter arguments into a dataset."""
    @wraps(method)
    def _impl(self, model=None, *args, **kwargs):
        filter_keys = ['filters', 'filter_blank', 'min_tiles']
        has_filters = any([k in kwargs for k in filter_keys])
        if model is not None:
            config = sf.util.get_model_config(model)
        if has_filters and 'dataset' in kwargs:
            k_s = ', '.join(filter_keys)
            raise errors.ProjectError(
                f"Cannot supply both `dataset` and filter arguments ({k_s})."
                " Instead, supply a filtered dataset (Dataset.filter(...))"
            )
        if 'dataset' in kwargs:
            if model is not None:
                kwargs['dataset']._assert_size_matches_hp(config['hp'])
                return method(self, model, *args, **kwargs)
            else:
                return method(self, *args, **kwargs)
        else:
            if model is None:
                raise errors.ProjectError("Missing argument 'model'.")
            dataset = self.dataset(
                tile_px=config['hp']['tile_px'],
                tile_um=config['hp']['tile_um'],
                **{k: v for k, v in kwargs.items() if k in filter_keys},
                verification='slides'
            )
            return method(self, model, *args, dataset=dataset, **kwargs)
    return _impl


def _project_config(
    name: str = 'MyProject',
    annotations: str = './annotations.csv',
    dataset_config: str = './datasets.json',
    sources: Optional[Union[str, List[str]]] = None,
    models_dir: str = './models',
    eval_dir: str = './eval'
) -> Dict:
    args = locals()
    args['slideflow_version'] = sf.__version__
    if sources is None:
        args['sources'] = []
    elif isinstance(sources, str):
        args['sources'] = [sources]
    return args


def _heatmap_worker(
    slide: str,
    args: SimpleNamespace,
    kwargs: Any
) -> None:
    """Heatmap worker for :meth:`slideflow.Project.generate_heatmaps.`

    Any function loading a slide must be kept in an isolated process, as
    loading more than one slide in a single process causes instability / hangs.
    I suspect this is a libvips or openslide issue but I haven't been able to
    identify the root cause. Isolating processes when multiple slides are to be
    processed sequentially is a workaround, hence the process-isolated worker.

    Args:
        slide (str): Path to slide.
        args (SimpleNamespace): Namespace of heatmap arguments.
        kwargs (dict): kwargs for heatmap.save()
    """
    sf.setLoggingLevel(args.verbosity)
    heatmap = sf.Heatmap(slide,
                         model=args.model,
                         stride_div=args.stride_div,
                         rois=args.rois,
                         roi_method=args.roi_method,
                         batch_size=args.batch_size,
                         img_format=args.img_format,
                         num_threads=args.num_threads)
    heatmap.save(args.outdir, **kwargs)


def _train_worker(
    datasets: Tuple[sf.Dataset, sf.Dataset],
    model_kw: Dict,
    training_kw: Dict,
    results_dict: Dict,
    verbosity: int
) -> None:
    """Internal function to execute model training in an isolated process."""
    sf.setLoggingLevel(verbosity)
    train_dts, val_dts = datasets
    trainer = sf.model.trainer_from_hp(**model_kw)
    results = trainer.train(train_dts, val_dts, **training_kw)
    results_dict.update({model_kw['name']: results})


def _setup_input_labels(
    dts: sf.Dataset,
    inpt_headers: List[str],
    val_dts: Optional[sf.Dataset] = None
) -> Tuple[Dict, List[int], Dict]:
    '''
    Args:
        dts (:class:`slideflow.Dataset`): Training dataset.
        inpt_headers (list(str)): Annotation headers for slide-level input.
        val_dts (:class:`slideflow.Dataset`, optional): Validation dataset.
            Used for harmonizing categorical labels to ensure consistency.
    '''
    # Dict mapping input headers to # of labels
    feature_len = {}
    # Nested dict mapping input vars to either category ID dicts or 'float'
    inpt_classes = {}  # type: Dict
    # Dict mapping slide names to slide-level model input
    model_inputs = defaultdict(list)  # type: Dict
    for inpt in inpt_headers:
        if val_dts is not None:
            is_float = dts.is_float(inpt) and val_dts.is_float(inpt)
        else:
            is_float = dts.is_float(inpt)
        kind = 'float' if is_float else 'categorical'
        log.info(f"Adding input variable [blue]{inpt}[/] as {kind}")

        labels, unique = dts.labels(inpt, use_float=is_float)
        slides = list(labels.keys())

        if is_float:
            feature_len[inpt] = 1
            inpt_classes[inpt] = 'float'
            for slide in slides:
                model_inputs[slide] += [labels[slide]]
        else:
            feature_len[inpt] = len(unique)
            inpt_classes[inpt] = dict(zip(range(len(unique)), unique))
            for slide in slides:
                onehot_label = sf.util.to_onehot(
                    labels[slide], len(unique)  # type: ignore
                )
                # Concatenate onehot labels together
                model_inputs[slide] += list(onehot_label)

    feature_sizes = [feature_len[i] for i in inpt_headers]
    return inpt_classes, feature_sizes, model_inputs


def get_validation_settings(**kwargs: Any) -> SimpleNamespace:
    """Returns a namespace of validation settings.

    Args:
        strategy (str): Validation dataset selection strategy.
            Options include bootstrap, k-fold, k-fold-manual,
            k-fold-preserved-site, fixed, and none. Defaults to 'k-fold'.
        k_fold (int): Total number of K if using K-fold validation.
            Defaults to 3.
        k (int): Iteration of K-fold to train, starting at 1. Defaults to None
            (training all k-folds).
        k_fold_header (str): Annotations file header column for manually
            specifying k-fold. Only used if validation strategy is
            'k-fold-manual'. Defaults to None.
        k_fold_header (str): Annotations file header column for manually
            specifying k-fold or for preserved-site cross validation. Only used
            if validation strategy is 'k-fold-manual' or
            'k-fold-preserved-site'. Defaults to None for k-fold-manual and
            'site' for k-fold-preserved-site.
        fraction (float): Fraction of dataset to use for validation testing,
            if strategy is 'fixed'.
        source (str): Dataset source to use for validation.
            Defaults to None (same as training).
        annotations (str): Path to annotations file for validation dataset.
            Defaults to None (same as training).
        filters (dict): Filters dictionary to use for validation dataset.
            Defaults to None (same as training).

    """
    if 'strategy' in kwargs and kwargs['strategy'] == 'k-fold-preserved-site':
        default_header = 'site'
    else:
        default_header = None
    args_dict = {
        'strategy': 'k-fold',
        'k_fold': 3,
        'k': None,
        'k_fold_header': default_header,
        'fraction': None,
        'source': None,
        'annotations': None,
        'filters': None,
    }
    for k in kwargs:
        if k not in args_dict:
            raise ValueError(f"Unrecognized validation setting {k}")
        args_dict[k] = kwargs[k]
    args = SimpleNamespace(**args_dict)

    if args.strategy is None:
        args.strategy = 'none'
    if (args.k_fold_header is None and args.strategy == 'k-fold-manual'):
        raise ValueError(
            "val_strategy 'k-fold-manual' requires 'k_fold_header'"
        )
    return args


def add_source(
    name: str,
    slides: str,
    roi: str,
    tiles: str,
    tfrecords: str,
    path: str
) -> None:
    """Adds a dataset source to a dataset configuration file.

    Args:
        name (str): Source name.
        slides (str): Path to directory containing slides.
        roi (str): Path to directory containing CSV ROIs.
        tiles (str): Path to directory in which to store extracted tiles.
        tfrecords (str): Directory to store TFRecords of extracted tiles.
        path (str): Path to dataset configuration file.
    """

    try:
        datasets_data = sf.util.load_json(path)
    except FileNotFoundError:
        datasets_data = {}
    datasets_data.update({name: {
        'slides': slides,
        'roi': roi,
        'tiles': tiles,
        'tfrecords': tfrecords,
    }})
    sf.util.write_json(datasets_data, path)
    log.info(f'Saved dataset source {name} to {path}')


def load_sources(path: str) -> Tuple[Dict, List]:
    """Loads datasets configuration dictionaries from a datasets.json file."""
    try:
        sources_data = sf.util.load_json(path)
        sources = list(sources_data.keys())
        sources.sort()
    except FileNotFoundError:
        sources_data = {}
        sources = []
    return sources_data, sources


def interactive_project_setup(project_folder: str) -> Dict:
    """Guides user through project creation at the given folder,
    saving configuration to "settings.json".
    """
    if not exists(project_folder):
        os.makedirs(project_folder)
    project = {}  # type: Dict[str, Any]
    project['name'] = input('What is the project name? ')
    project['annotations'] = sf.util.path_input(
        'Annotations file location [./annotations.csv] ',
        root=project_folder,
        default='./annotations.csv',
        filetype='csv',
        verify=False
    )
    # Dataset configuration
    project['dataset_config'] = sf.util.path_input(
        'Dataset configuration file location [./datasets.json] ',
        root=project_folder,
        default='./datasets.json',
        filetype='json',
        verify=False
    )
    project['sources'] = []
    while not project['sources']:
        path = relative_path(project['dataset_config'], project_folder)
        datasets_data, sources = load_sources(path)
        print('[bold]Detected dataset sources:')
        if not len(sources):
            print(' [None]')
        else:
            for i, name in enumerate(sources):
                print(f' {i+1}. {name}')
            print(f' {len(sources)+1}. ADD NEW')
            valid_source_choices = [str(v) for v in range(1, len(sources)+2)]
            selection = sf.util.choice_input(
                'Which datasets should be used? ',
                valid_choices=valid_source_choices,
                multi_choice=True
            )
        if not len(sources) or str(len(sources)+1) in selection:
            # Create new dataset
            print(f"{'[bold]Creating new dataset source'}")
            source_name = input('What is the dataset source name? ')
            source_slides = sf.util.path_input(
                'Where are the slides stored? [./slides] ',
                root=project_folder,
                default='./slides',
                create_on_invalid=True
            )
            source_roi = sf.util.path_input(
                'Where are the ROI files (CSV) stored? [./slides] ',
                root=project_folder,
                default='./slides',
                create_on_invalid=True
            )
            source_tiles = sf.util.path_input(
                'Image tile storage location [./tiles] ',
                root=project_folder,
                default='./tiles',
                create_on_invalid=True
            )
            source_tfrecords = sf.util.path_input(
                'TFRecord storage location [./tfrecords] ',
                root=project_folder,
                default='./tfrecords',
                create_on_invalid=True
            )
            add_source(
                name=source_name,
                slides=relative_path(source_slides, project_folder),
                roi=relative_path(source_roi, project_folder),
                tiles=relative_path(source_tiles, project_folder),
                tfrecords=relative_path(source_tfrecords, project_folder),
                path=relative_path(project['dataset_config'], project_folder)
            )
            print('Updated dataset configuration file.')
        else:
            try:
                project['sources'] = [sources[int(j)-1] for j in selection]
            except TypeError:
                print(f'Invalid selection: {selection}')
                continue

    project['models_dir'] = sf.util.path_input(
        'Where should the saved models be stored? [./models] ',
        root=project_folder,
        default='./models',
        create_on_invalid=True
    )
    project['eval_dir'] = sf.util.path_input(
        'Where should model evaluations be stored? [./eval] ',
        root=project_folder,
        default='./eval',
        create_on_invalid=True
    )
    # Save settings as relative paths
    settings = _project_config(**project)
    sf.util.write_json(settings, join(project_folder, 'settings.json'))

    # Write a sample actions.py file
    sample_path = join(dirname(realpath(__file__)), 'sample_actions.py')
    with open(sample_path, 'r') as sample_file:
        sample_actions = sample_file.read()
        with open(join(project_folder, 'actions.py'), 'w') as actions_file:
            actions_file.write(sample_actions)
    log.info('Project configuration saved.')
    return settings
