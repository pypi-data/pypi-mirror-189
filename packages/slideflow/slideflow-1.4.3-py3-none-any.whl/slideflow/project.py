import copy
import csv
import itertools
import json
import multiprocessing
import numpy as np
import os
import shutil
import pickle
import tarfile
from tqdm import tqdm
from multiprocessing.managers import DictProxy
from os.path import basename, exists, join, dirname
from statistics import mean
from types import SimpleNamespace
from typing import (TYPE_CHECKING, Any, Callable, Dict, List, Optional, Tuple,
                    Union)

import slideflow as sf
from slideflow import errors, project_utils
from slideflow.dataset import Dataset
from slideflow.model import ModelParams
from slideflow.project_utils import auto_dataset, get_validation_settings
from slideflow.util import log, path_to_name, path_to_ext

if TYPE_CHECKING:
    import pandas as pd
    from ConfigSpace import ConfigurationSpace

    from slideflow.model import DatasetFeatures, Trainer


class Project:
    """Assists with project organization and execution of pipeline functions.

    Standard instantiation with __init__ assumes a project already exists at
    a given directory, or that configuration will be supplied via kwargs.
    Alternatively, a project may be instantiated using :meth:`from_prompt`,
    which interactively guides users through configuration.

    *Interactive instantiation:*

    .. code-block:: python

        >>> import slideflow as sf
        >>> P = sf.Project.from_prompt('/project/path')
        What is the project name?

    *Manual configuration:*

    .. code-block:: python

        >>> import slideflow as sf
        >>> P = sf.Project('/project/path', name=..., ...)

    """

    def __init__(self, root: str, use_neptune: bool = False, **kwargs) -> None:
        """Initializes project at the specified project folder, creating a new
        project using the specified kwargs if one does not already exist.
        Will create a blank annotations with slide names if one does not exist.

        Args:
            root (str): Path to project directory.

        Keyword Args:
            name (str): Project name. Defaults to 'MyProject'.
            annotations (str): Path to annotations CSV file.
                Defaults to './annotations.csv'
            dataset_config (str): Path to dataset configuration JSON file.
                Defaults to './datasets.json'.
            sources (list(str)): List of dataset sources to include in project.
                Defaults to 'source1'.
            models_dir (str): Path to directory in which to save models.
                Defaults to './models'.
            eval_dir (str): Path to directory in which to save evaluations.
                Defaults to './eval'.

        Raises:
            slideflow.errors.ProjectError: if project folder does not exist,
                or the folder exists but kwargs are provided.
        """

        self.root = root

        if sf.util.is_project(root) and kwargs:
            raise errors.ProjectError(f"Project already exists at {root}")
        elif sf.util.is_project(root):
            self.load_project(root)
        elif kwargs:
            log.info(f"Creating project at {root}...")
            self._settings = project_utils._project_config(**kwargs)
            if not exists(root):
                os.makedirs(root)
            self.save()
        else:
            raise errors.ProjectError(f"Project folder {root} does not exist.")

        # Create directories, if not already made
        if not exists(self.models_dir):
            os.makedirs(self.models_dir)
        if not exists(self.eval_dir):
            os.makedirs(self.eval_dir)

        # Create blank annotations file if one does not exist
        if not exists(self.annotations) and exists(self.dataset_config):
            self.create_blank_annotations()

        # Neptune
        self.use_neptune = use_neptune

    @classmethod
    def from_prompt(cls, root: str, **kwargs: Any) -> "Project":
        """Initializes project by creating project folder, prompting user for
        project settings, and saving to "settings.json" in project directory.

        Args:
            root (str): Path to project directory.
        """

        if not sf.util.is_project(root):
            log.info(f'Setting up new project at "{root}"')
            project_utils.interactive_project_setup(root)
        obj = cls(root, **kwargs)
        return obj

    def __repr__(self):
        if self.use_neptune:
            tail = ", use_neptune={!r}".format(self.use_neptune)
        else:
            tail = ''
        return "Project(root={!r}{})".format(self.root, tail)

    @property
    def verbosity(self) -> int:
        return sf.getLoggingLevel()

    @property
    def annotations(self) -> str:
        """Path to annotations file."""
        return self._read_relative_path(self._settings['annotations'])

    @annotations.setter
    def annotations(self, val: str) -> None:
        if not isinstance(val, str):
            raise errors.ProjectError("'annotations' must be a path.")
        self._settings['annotations'] = val

    @property
    def dataset_config(self) -> str:
        """Path to dataset configuration JSON file."""
        return self._read_relative_path(self._settings['dataset_config'])

    @dataset_config.setter
    def dataset_config(self, val: str) -> None:
        if not isinstance(val, str):
            raise errors.ProjectError("'dataset_config' must be path to JSON.")
        self._settings['dataset_config'] = val

    @property
    def eval_dir(self) -> str:
        """Path to evaluation directory."""
        if 'eval_dir' not in self._settings:
            log.debug("Missing eval_dir in project settings, Assuming ./eval")
            return self._read_relative_path('./eval')
        else:
            return self._read_relative_path(self._settings['eval_dir'])

    @eval_dir.setter
    def eval_dir(self, val: str) -> None:
        if not isinstance(val, str):
            raise errors.ProjectError("'eval_dir' must be a path")
        self._settings['eval_dir'] = val

    @property
    def models_dir(self) -> str:
        """Path to models directory."""
        return self._read_relative_path(self._settings['models_dir'])

    @models_dir.setter
    def models_dir(self, val: str) -> None:
        if not isinstance(val, str):
            raise errors.ProjectError("'models_dir' must be a path")
        self._settings['models_dir'] = val

    @property
    def name(self) -> str:
        """Descriptive project name."""
        return self._settings['name']

    @name.setter
    def name(self, val: str) -> None:
        if not isinstance(val, str):
            raise errors.ProjectError("'name' must be a str")
        self._settings['name'] = val

    @property
    def neptune_workspace(self) -> Optional[str]:
        """Neptune workspace name."""
        if 'neptune_workspace' in self._settings:
            return self._settings['neptune_workspace']
        elif 'NEPTUNE_WORKSPACE' in os.environ:
            return os.environ['NEPTUNE_WORKSPACE']
        else:
            return None

    @neptune_workspace.setter
    def neptune_workspace(self, name: str) -> None:
        """Neptune workspace name."""
        if not isinstance(name, str):
            raise errors.ProjectError('Neptune workspace must be a string.')
        self._settings['neptune_workspace'] = name

    @property
    def neptune_api(self) -> Optional[str]:
        """Neptune API token."""
        if 'neptune_api' in self._settings:
            return self._settings['neptune_api']
        elif 'NEPTUNE_API_TOKEN' in os.environ:
            return os.environ['NEPTUNE_API_TOKEN']
        else:
            return None

    @neptune_api.setter
    def neptune_api(self, api_token: str) -> None:
        """Neptune API token."""
        if not isinstance(api_token, str):
            raise errors.ProjectError('API token must be a string.')
        self._settings['neptune_api'] = api_token

    @property
    def sources(self) -> List[str]:
        """Returns list of dataset sources active in this project."""
        if 'sources' in self._settings:
            return self._settings['sources']
        elif 'datasets' in self._settings:
            log.debug("'sources' misnamed 'datasets' in project settings.")
            return self._settings['datasets']
        else:
            raise ValueError('Unable to find project dataset sources')

    @sources.setter
    def sources(self, v: List[str]) -> None:
        if not isinstance(v, list) or any([not isinstance(v, str) for v in v]):
            raise errors.ProjectError("'sources' must be a list of str")
        self._settings['sources'] = v

    def _read_relative_path(self, path: str) -> str:
        """Converts relative path within project directory to global path."""
        return sf.util.relative_path(path, self.root)

    def _setup_labels(
        self,
        dataset: Dataset,
        hp: ModelParams,
        outcomes: List[str],
        config: Dict,
        splits: str,
        eval_k_fold: Optional[int] = None
    ) -> Tuple[Dataset, Dict, Union[Dict, List]]:
        '''Prepares dataset and labels.'''

        # Assign labels into int
        conf_labels = config['outcome_labels']
        if hp.model_type() == 'categorical':
            if len(outcomes) == 1 and outcomes[0] not in conf_labels:
                outcome_label_to_int = {
                    outcomes[0]: {
                        v: int(k) for k, v in conf_labels.items()
                    }
                }
            else:
                outcome_label_to_int = {
                    o: {
                        v: int(k) for k, v in conf_labels[o].items()
                    } for o in conf_labels
                }
        else:
            outcome_label_to_int = None

        # Get patient-level labels
        use_float = (hp.model_type() in ['linear', 'cph'])
        labels, unique = dataset.labels(
            outcomes,
            use_float=use_float,
            assign=outcome_label_to_int
        )
        # Prepare labels for validation splitting
        if hp.model_type() == 'categorical' and len(outcomes) > 1:
            def process_label(v):
                return '-'.join(map(str, v)) if isinstance(v, list) else v
            split_labels = {k: process_label(v) for k, v in labels.items()}
        else:
            split_labels = labels

        # If using a specific k-fold, load validation plan
        if eval_k_fold:
            log.info(f"Using k-fold iteration {eval_k_fold}")
            _, eval_dts = dataset.train_val_split(
                hp.model_type(),
                split_labels,
                val_strategy=config['validation_strategy'],
                splits=join(self.root, splits),
                val_fraction=config['validation_fraction'],
                val_k_fold=config['validation_k_fold'],
                k_fold_iter=eval_k_fold
            )
            return eval_dts, labels, unique

        # Otherwise use all TFRecords
        else:
            return dataset, labels, unique

    def _prepare_trainer(
        self,
        model: str,
        dataset: Dataset,
        outcomes: Optional[Union[str, List[str]]] = None,
        checkpoint: Optional[str] = None,
        eval_k_fold: Optional[int] = None,
        splits: str = "splits.json",
        max_tiles: int = 0,
        mixed_precision: bool = True,
        allow_tf32: bool = False,
        input_header: Optional[Union[str, List[str]]] = None,
        load_method: str = 'full',
        custom_objects: Optional[Dict[str, Any]] = None,
    ) -> Tuple["Trainer", Dataset]:
        """Prepares a :class:`slideflow.model.Trainer` for eval or prediction.

        Args:
            model (str): Path to model to evaluate.
            dataset (:class:`slideflow.dataset.Dataset`): Dataset
                from which to generate activations.
            outcomes (str): Str or list of str. Annotation column
                header specifying the outcome label(s).
            checkpoint (str, optional): Path to cp.ckpt file, if evaluating
                saved checkpoint. Defaults to None.
            eval_k_fold (int, optional): K-fold iteration number to evaluate.
                Defaults to None. If None, evaluate all tfrecords.
            splits (str, optional): Filename of JSON file in which to log
                training/validation splits. Looks for filename in project root.
                Defaults to "splits.json".
            max_tiles (int, optional): Maximum number of tiles from each slide
                to evaluate. Defaults to 0 (include all tiles).
            mixed_precision (bool, optional): Enable mixed precision.
                Defaults to True.
            allow_tf32 (bool): Allow internal use of Tensorfloat-32 format.
                Defaults to False.
            input_header (str, optional): Annotation column header to use as
                additional input. Defaults to None.
            load_method (str): Either 'full' or 'weights'. Method to use
                when loading a Tensorflow model. If 'full', loads the model with
                ``tf.keras.models.load_model()``. If 'weights', will read the
                ``params.json``configuration file, build the model architecture,
                and then load weights from the given model with
                ``Model.load_weights()``. Loading with 'full' may improve
                compatibility across Slideflow versions. Loading with 'weights'
                may improve compatibility across hardware & environments.
            custom_objects (dict, Optional): Dictionary mapping names
                (strings) to custom classes or functions. Defaults to None.

        Returns:
            A tuple containing

                :class:`slideflow.model.Trainer`: Trainer.

                :class:`slideflow.Dataset`: Evaluation dataset.
        """

        if eval_k_fold is not None and outcomes is None:
            raise ValueError('`eval_k_fold` invalid when predicting.')

        # Load hyperparameters from saved model
        config = sf.util.get_model_config(model)
        hp = ModelParams()
        hp.load_dict(config['hp'])
        model_name = f"eval-{basename(model)}"

        # If not provided, detect outcomes from model config
        predicting = (outcomes is None)
        if predicting:
            outcomes = config['outcomes']

        assert outcomes is not None
        outcomes = sf.util.as_list(outcomes)

        # Filter out slides that are blank in the outcome label,
        # or blank in any of the input_header categories
        filter_blank = [o for o in outcomes]
        if input_header is not None and not isinstance(input_header, list):
            input_header = [input_header]
        if input_header is not None:
            filter_blank += input_header

        # Set up outcome labels
        if not predicting:
            dataset = dataset.filter(filter_blank=filter_blank)
            eval_dts, labels, unique = self._setup_labels(
                dataset, hp, outcomes, config, splits, eval_k_fold=eval_k_fold
            )
        else:
            eval_dts = dataset
            if sf.backend() == 'torch':
                labels = config['outcome_labels']
            else:
                labels = {}
            unique = list(config['outcome_labels'].values())

        # Set max tiles
        eval_dts = eval_dts.clip(max_tiles)

        # Prepare additional slide-level input
        if input_header:
            _res = project_utils._setup_input_labels(eval_dts, input_header)
            inpt_labels, feature_sizes, slide_inp = _res
        else:
            inpt_labels = None
            feature_sizes = None
            slide_inp = {}

        n_feat = 0 if feature_sizes is None else sum(feature_sizes)
        if feature_sizes and n_feat != sum(config['input_feature_sizes']):
            n_model_feat = sum(config['input_feature_sizes'])
            raise ValueError(
                f'Patient feature matrix (size {n_feat}) '
                f'is different from model (size {n_model_feat}).'
            )

        # Log model settings and hyperparameters
        if hp.model_type() == 'categorical':
            outcome_labels = dict(zip(range(len(unique)), unique))
        else:
            outcome_labels = None

        model_dir = sf.util.get_new_model_dir(self.eval_dir, model_name)

        # Set missing validation keys to NA
        for v_end in ('strategy', 'fraction', 'k_fold'):
            val_key = f'validation_{v_end}'
            if val_key not in config:
                config[val_key] = 'NA'

        eval_config = {
            'slideflow_version': sf.__version__,
            'project': self.name,
            'backend': sf.backend(),
            'git_commit': sf.__gitcommit__,
            'model_name': model_name,
            'model_path': model,
            'stage': 'evaluation',
            'img_format': config['img_format'],
            'tile_px': hp.tile_px,
            'tile_um': hp.tile_um,
            'model_type': hp.model_type(),
            'outcomes': outcomes,
            'input_features': input_header,
            'input_feature_sizes': feature_sizes,
            'input_feature_labels': inpt_labels,
            'outcome_labels': outcome_labels,
            'dataset_config': self.dataset_config,
            'sources': self.sources,
            'annotations': self.annotations,
            'validation_strategy': config['validation_strategy'],
            'validation_fraction': config['validation_fraction'],
            'validation_k_fold': config['validation_k_fold'],
            'k_fold_i': eval_k_fold,
            'filters': dataset.filters,
            'pretrain': None,
            'resume_training': None,
            'checkpoint': checkpoint,
            'hp': hp.get_dict(),
            'max_tiles': max_tiles,
            'min_tiles': dataset.min_tiles,
        }
        if 'norm_fit' in config:
            eval_config.update({'norm_fit': config['norm_fit']})

        # Build a model using the slide list as input
        # and the annotations dictionary as output labels
        trainer = sf.model.trainer_from_hp(
            hp,
            outdir=model_dir,
            labels=labels,
            config=eval_config,
            patients=dataset.patients(),
            slide_input=slide_inp,
            manifest=dataset.manifest(),
            mixed_precision=mixed_precision,
            allow_tf32=allow_tf32,
            feature_names=input_header,
            feature_sizes=feature_sizes,
            outcome_names=outcomes,
            use_neptune=self.use_neptune,
            neptune_api=self.neptune_api,
            neptune_workspace=self.neptune_workspace,
            load_method=load_method,
            custom_objects=custom_objects,
        )
        if isinstance(model, str):
            trainer.load(model)
        if checkpoint:
            n_features = 0 if not feature_sizes else sum(feature_sizes)
            trainer.model = hp.build_model(
                labels=labels,
                num_slide_features=n_features
            )
            trainer.model.load_weights(checkpoint)

        return trainer, eval_dts

    def _train_hp(
        self,
        *,
        hp_name: str,
        hp: ModelParams,
        outcomes: List[str],
        val_settings: SimpleNamespace,
        ctx: multiprocessing.context.BaseContext,
        filters: Optional[Dict],
        filter_blank: Optional[Union[str, List[str]]],
        input_header: Optional[Union[str, List[str]]],
        min_tiles: int,
        max_tiles: int,
        mixed_precision: bool,
        allow_tf32: bool,
        splits: str,
        results_dict: Union[Dict, DictProxy],
        training_kwargs: Dict,
        balance_headers: Optional[Union[str, List[str]]],
        process_isolate: bool = False,
        **kwargs
    ) -> None:
        '''Trains a model(s) using the specified hyperparameters.

        Keyword Args:
            hp_name (str): Name of hyperparameter combination being run.
            hp (:class:`slideflow.ModelParams`): Model parameters.
            outcomes (str or list(str)): Annotation outcome headers.
            val_settings (:class:`types.SimpleNamspace`): Validation settings.
            ctx (multiprocessing.Context): Multiprocessing context for sharing
                results from isolated training processes.
            filters (dict): Dataset filters.
            filter_blank (list): Excludes slides blank in this annotation col.
            input_header (str or list(str)): Annotation col of additional
                slide-level input.
            min_tiles (int): Only includes tfrecords with >= min_tiles
            max_tiles (int): Cap maximum tiles per tfrecord.
            mixed_precision (bool): Train with mixed precision.
            allow_tf32 (bool): Allow internal use of Tensorfloat-32 format.
                Defaults to False.
            splits (str): Location of splits file for logging/reading splits.
            balance_headers (str, list(str)): Annotation col headers for
                mini-batch balancing.
            results_dict (dict): Multiprocessing-friendly dict for sending
                results from isolated training processes
            training_kwargs (dict): Keyword arguments for Trainer.train().
        '''

        # --- Prepare dataset ---------------------------------------------
        # Filter out slides that are blank in the outcome label,
        # or blank in any of the input_header categories
        if filter_blank is not None and not isinstance(filter_blank, list):
            filter_blank = [filter_blank]
        if filter_blank:
            filter_blank += [o for o in outcomes]
        else:
            filter_blank = [o for o in outcomes]
        if input_header is not None and not isinstance(input_header, list):
            input_header = [input_header]
        if input_header is not None:
            filter_blank += input_header
        dataset = self.dataset(hp.tile_px, hp.tile_um)
        dataset = dataset.filter(
            filters=filters,
            filter_blank=filter_blank,
            min_tiles=min_tiles
        )
        # --- Load labels -------------------------------------------------
        use_float = (hp.model_type() in ['linear', 'cph'])
        labels, unique = dataset.labels(outcomes, use_float=use_float)
        if hp.model_type() == 'categorical' and len(outcomes) == 1:
            outcome_labels = dict(zip(range(len(unique)), unique))
        elif hp.model_type() == 'categorical':
            assert isinstance(unique, dict)
            outcome_labels = {
                k: dict(zip(range(len(ul)), ul))  # type: ignore
                for k, ul in unique.items()
            }
        else:
            outcome_labels = dict(zip(range(len(outcomes)), outcomes))
        if hp.model_type() != 'linear' and len(outcomes) > 1:
            log.info('Using multi-outcome approach for categorical outcome')

        # If multiple categorical outcomes are used,
        # create a merged variable for k-fold splitting
        if hp.model_type() == 'categorical' and len(outcomes) > 1:
            split_labels = {
                k: '-'.join(map(str, v))  # type: ignore
                for k, v in labels.items()
            }
        else:
            split_labels = labels  # type: ignore

        # --- Prepare k-fold validation configuration ---------------------
        results_log_path = os.path.join(self.root, 'results_log.csv')
        k_header = val_settings.k_fold_header
        if val_settings.k is not None and not isinstance(val_settings.k, list):
            val_settings.k = [val_settings.k]
        if val_settings.strategy == 'k-fold-manual':
            _, unique_k = dataset.labels(k_header, format='name')
            valid_k = [kf for kf in unique_k]
            k_fold = len(valid_k)
            log.info(f"Manual folds: {', '.join([str(ks) for ks in valid_k])}")
            if val_settings.k:
                valid_k = [kf for kf in valid_k if kf in val_settings.k]
        elif val_settings.strategy in ('k-fold',
                                       'k-fold-preserved-site',
                                       'bootstrap'):
            k_fold = val_settings.k_fold
            if val_settings.k is None:
                valid_k = list(range(1, k_fold+1))
            else:
                valid_k = [
                    kf for kf in range(1, k_fold+1) if kf in val_settings.k
                ]
        else:
            k_fold = 0
            valid_k = [None]  # type: ignore

        # Create model labels
        label_string = '-'.join(outcomes)
        model_name = f'{label_string}-{hp_name}'
        if k_fold is None:
            model_iterations = [model_name]
        else:
            model_iterations = [f'{model_name}-kfold{k}' for k in valid_k]

        s_args = SimpleNamespace(
            model_name=model_name,
            outcomes=outcomes,
            k_header=k_header,
            valid_k=valid_k,
            split_labels=split_labels,
            splits=splits,
            labels=labels,
            min_tiles=min_tiles,
            max_tiles=max_tiles,
            outcome_labels=outcome_labels,
            filters=filters,
            training_kwargs=training_kwargs,
            mixed_precision=mixed_precision,
            allow_tf32=allow_tf32,
            ctx=ctx,
            results_dict=results_dict,
            bal_headers=balance_headers,
            input_header=input_header,
            process_isolate=process_isolate,
            **kwargs
        )

        # --- Train on a specific K-fold --------------------------------------
        for k in valid_k:
            s_args.k = k
            self._train_split(dataset, hp, val_settings, s_args)

        # --- Record results --------------------------------------------------
        if (not val_settings.source
            and (val_settings.strategy is None
                 or val_settings.strategy == 'none')):
            log.info(f'No validation performed.')
        else:
            for mi in model_iterations:
                if mi not in results_dict or 'epochs' not in results_dict[mi]:
                    log.error(f'Training failed for model {model_name}')
                else:
                    sf.util.update_results_log(
                        results_log_path,
                        mi,
                        results_dict[mi]['epochs']
                    )
            log.info(f'Training results saved: [green]{results_log_path}')

    def _train_split(
        self,
        dataset: Dataset,
        hp: ModelParams,
        val_settings: SimpleNamespace,
        s_args: SimpleNamespace
    ) -> None:
        '''Trains a model for a given training/validation split.

        Args:
            dataset (:class:`slideflow.Dataset`): Dataset to split into
                training and validation.
            hp (:class:`slideflow.ModelParams`): Model parameters.
            val_settings (:class:`types.SimpleNamspace`): Validation settings.
            s_args (:class:`types.SimpleNamspace`): Training settings.
        '''

        # Log current model name and k-fold iteration, if applicable
        k_msg = ''
        if s_args.k is not None:
            k_msg = f' ({val_settings.strategy} #{s_args.k})'
        if sf.getLoggingLevel() <= 20:
            print()
        log.info(f'Training model [bold]{s_args.model_name}[/]{k_msg}...')
        log.info(f'Hyperparameters: {hp}')
        log.info(f'Val settings: {json.dumps(vars(val_settings), indent=2)}')

        # --- Set up validation data ------------------------------------------
        manifest = dataset.manifest()
        from_wsi = ('from_wsi' in s_args.training_kwargs
                    and s_args.training_kwargs['from_wsi'])

        # Use an external validation dataset if supplied
        if val_settings.source:
            train_dts = dataset
            val_dts = Dataset(
                tile_px=hp.tile_px,
                tile_um=hp.tile_um,
                config=self.dataset_config,
                sources=val_settings.source,
                annotations=val_settings.annotations,
                filters=val_settings.filters,
                filter_blank=val_settings.filter_blank
            )
            is_float = (hp.model_type() in ['linear', 'cph'])
            val_labels, _ = val_dts.labels(s_args.outcomes, use_float=is_float)
            s_args.labels.update(val_labels)
        # Use manual k-fold assignments if indicated
        elif val_settings.strategy == 'k-fold-manual':
            t_filters = {
                s_args.k_header: [j for j in s_args.valid_k if j != s_args.k]
            }
            train_dts = dataset.filter(t_filters)
            val_dts = dataset.filter(filters={s_args.k_header: [s_args.k]})
        # No validation
        elif val_settings.strategy == 'none':
            train_dts = dataset
            val_dts = None
        # Otherwise, calculate k-fold splits
        else:
            if val_settings.strategy == 'k-fold-preserved-site':
                site_labels = dataset.labels(
                    s_args.k_header,
                    format='name'
                )[0]  # type: Any
            else:
                site_labels = None
            train_dts, val_dts = dataset.train_val_split(
                hp.model_type(),
                s_args.split_labels,
                val_strategy=val_settings.strategy,
                splits=join(self.root, s_args.splits),
                val_fraction=val_settings.fraction,
                val_k_fold=val_settings.k_fold,
                k_fold_iter=s_args.k,
                site_labels=site_labels,
                from_wsi=from_wsi
            )

        # ---- Balance and clip datasets --------------------------------------
        if s_args.bal_headers is None:
            s_args.bal_headers = s_args.outcomes
        if not from_wsi:
            train_dts = train_dts.balance(
                s_args.bal_headers,
                hp.training_balance,
            )
            train_dts = train_dts.clip(s_args.max_tiles)
        elif hp.training_balance not in ('none', None) or s_args.max_tiles:
            log.warning("Balancing / clipping is disabled when `from_wsi=True`")

        if val_dts and not from_wsi:
            val_dts = val_dts.balance(
                s_args.bal_headers,
                hp.validation_balance,
            )
            val_dts = val_dts.clip(s_args.max_tiles)

        if from_wsi:
            num_train = len(train_dts.slide_paths())
            num_val = 0 if not val_dts else len(val_dts.slide_paths())
            log.info(f'Using {num_train} training slides, {num_val} validation')
        else:
            num_train = len(train_dts.tfrecords())
            num_val = 0 if not val_dts else len(val_dts.tfrecords())
            log.info(f'Using {num_train} training TFRecords, {num_val} validation')

        # --- Prepare additional slide-level input ----------------------------
        if s_args.input_header:
            _res = project_utils._setup_input_labels(
                dataset,
                s_args.input_header,
                val_dts=val_dts
            )
            inpt_labels, feature_sizes, slide_inp = _res
        else:
            inpt_labels = None
            feature_sizes = None
            slide_inp = None

        # --- Initialize model ------------------------------------------------
        # Using the project annotation file, assemble slides for training,
        # as well as the slide annotations dictionary (output labels)
        full_name = s_args.model_name
        if s_args.k is not None:
            full_name += f'-kfold{s_args.k}'
        model_dir = sf.util.get_new_model_dir(self.models_dir, full_name)

        # Log model settings and hyperparameters
        config = {
            'slideflow_version': sf.__version__,
            'project': self.name,
            'backend': sf.backend(),
            'git_commit': sf.__gitcommit__,
            'model_name': s_args.model_name,
            'full_model_name': full_name,
            'stage': 'training',
            'img_format': train_dts.img_format,
            'tile_px': hp.tile_px,
            'tile_um': hp.tile_um,
            'max_tiles': s_args.max_tiles,
            'min_tiles': s_args.min_tiles,
            'model_type': hp.model_type(),
            'outcomes': s_args.outcomes,
            'input_features': s_args.input_header,
            'input_feature_sizes': feature_sizes,
            'input_feature_labels': inpt_labels,
            'outcome_labels': s_args.outcome_labels,
            'dataset_config': self.dataset_config,
            'sources': self.sources,
            'annotations': self.annotations,
            'validation_strategy': val_settings.strategy,
            'validation_fraction': val_settings.fraction,
            'validation_k_fold': val_settings.k_fold,
            'k_fold_i': s_args.k,
            'filters': s_args.filters,
            'hp': hp.get_dict(),
            'training_kwargs': s_args.training_kwargs,
        }
        model_kwargs = {
            'hp': hp,
            'name': full_name,
            'manifest': manifest,
            'feature_names': s_args.input_header,
            'feature_sizes': feature_sizes,
            'outcome_names': s_args.outcomes,
            'outdir': model_dir,
            'config': config,
            'patients': dataset.patients(),
            'slide_input': slide_inp,
            'labels': s_args.labels,
            'mixed_precision': s_args.mixed_precision,
            'allow_tf32': s_args.allow_tf32,
            'use_neptune': self.use_neptune,
            'neptune_api': self.neptune_api,
            'neptune_workspace': self.neptune_workspace,
            'load_method': s_args.load_method
        }
        if s_args.process_isolate:
            process = s_args.ctx.Process(target=project_utils._train_worker,
                                        args=((train_dts, val_dts),
                                            model_kwargs,
                                            s_args.training_kwargs,
                                            s_args.results_dict,
                                            self.verbosity))
            process.start()
            log.debug(f'Spawning training process (PID: {process.pid})')
            process.join()
        else:
            project_utils._train_worker(
                (train_dts, val_dts),
                model_kwargs,
                s_args.training_kwargs,
                s_args.results_dict,
                self.verbosity
            )

    def add_source(
        self,
        name: str,
        *,
        slides: str,
        roi: str,
        tiles: str,
        tfrecords: str,
        path: Optional[str] = None
    ) -> None:
        """Adds a dataset source to the dataset configuration file.

        Args:
            name (str): Dataset source name.

        Keyword Args:
            slides (str): Path to directory containing slides.
            roi (str): Path to directory containing CSV ROIs.
            tiles (str): Path to directory for storing extracted tiles.
            tfrecords (str): Path to directory for storing TFRecords of tiles.
            path (str, optional): Path to dataset configuration file.
                Defaults to None. If not provided, uses project default.
        """

        if not path:
            path = self.dataset_config
        project_utils.add_source(name, slides, roi, tiles, tfrecords, path)
        if name not in self.sources:
            self.sources += [name]
        self.save()

    def associate_slide_names(self) -> None:
        """Automatically associate patients with slides in the annotations."""
        dataset = self.dataset(tile_px=0, tile_um=0, verification=None)
        dataset.update_annotations_with_slidenames(self.annotations)

    def create_blank_annotations(
        self,
        filename: Optional[str] = None
    ) -> None:
        """Creates an empty annotations file.

        Args:
            filename (str): Annotations file destination. If not provided,
                will use project default.
        """

        if filename is None:
            filename = self.annotations
        if exists(filename):
            raise errors.AnnotationsError(
                f"Error creating annotations {filename}; file already exists"
            )
        if not exists(self.dataset_config):
            raise errors.AnnotationsError(
                f"Dataset config {self.dataset_config} missing."
            )
        dataset = Dataset(
            config=self.dataset_config,
            sources=self.sources,
            tile_px=None,
            tile_um=None,
            annotations=None
        )
        all_paths = dataset.slide_paths(apply_filters=False)
        slides = [path_to_name(s) for s in all_paths]
        with open(filename, 'w') as csv_outfile:
            csv_writer = csv.writer(csv_outfile, delimiter=',')
            header = ['patient', 'dataset', 'category']
            csv_writer.writerow(header)
            for slide in slides:
                csv_writer.writerow([slide, '', ''])
        log.info(f"Wrote annotations file to [green]{filename}")

    def create_hp_sweep(
        self,
        filename: str = 'sweep.json',
        label: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        """Prepares a grid-search hyperparameter sweep, saving to a config file.

        To initiate a grid-search sweep using the created JSON file, pass
        this file to the ``params`` argument of ``Project.train()``:

            >>> P.train('outcome', params='sweep.json', ...)

        Args:
            filename (str, optional): Filename for hyperparameter sweep.
                Overwrites existing files. Saves in project root directory.
                Defaults to "sweep.json".
            label (str, optional): Label to use when naming models in sweep.
                Defaults to None.
            **kwargs: Parameters to include in the sweep. Parameters may either
                be fixed or provided as lists.
        """
        non_epoch_kwargs = {k: v for k, v in kwargs.items() if k != 'epochs'}
        pdict = copy.deepcopy(non_epoch_kwargs)
        args = list(pdict.keys())
        for arg in args:
            if not isinstance(pdict[arg], list):
                pdict[arg] = [pdict[arg]]
        argsv = list(pdict.values())
        sweep = list(itertools.product(*argsv))
        label = '' if not label else f'{label}-'
        hp_list = []
        for i, params in enumerate(sweep):
            full_params = dict(zip(args, list(params)))
            if 'epochs' in kwargs:
                full_params['epochs'] = kwargs['epochs']
            mp = ModelParams(**full_params)
            hp_list += [{f'{label}HPSweep{i}': mp.get_dict()}]
        sf.util.write_json(hp_list, os.path.join(self.root, filename))
        log.info(f'Wrote hp sweep (len {len(sweep)}) to [green]{filename}')

    def create_hyperparameter_sweep(self, *args: Any, **kwargs: Any) -> None:
        log.warn(
            "Deprecation warning: Project.create_hyperparameter_sweep() will"
            " be removed in slideflow>=1.2. Use Project.create_hp_sweep()."
        )
        self.create_hp_sweep(*args, **kwargs)

    @auto_dataset
    def evaluate(
        self,
        model: str,
        outcomes: Union[str, List[str]],
        *,
        dataset: Dataset,
        filters: Optional[Dict] = None,
        filter_blank: Optional[Union[str, List[str]]] = None,
        min_tiles: int = 0,
        checkpoint: Optional[str] = None,
        eval_k_fold: Optional[int] = None,
        splits: str = "splits.json",
        max_tiles: int = 0,
        mixed_precision: bool = True,
        allow_tf32: bool = False,
        input_header: Optional[Union[str, List[str]]] = None,
        load_method: str = 'full',
        custom_objects: Optional[Dict[str, Any]] = None,
        **kwargs: Any
    ) -> Dict:
        """Evaluates a saved model on a given set of tfrecords.

        Args:
            model (str): Path to model to evaluate.
            outcomes (str): Str or list of str. Annotation column
                header specifying the outcome label(s).

        Keyword Args:
            dataset (:class:`slideflow.dataset.Dataset`, optional): Dataset
                to evaluate. If not supplied, will evaluate all project
                tfrecords at the tile_px/tile_um matching the supplied model,
                optionally using provided filters and filter_blank.
            filters (dict, optional): Filters dict to use when selecting
                tfrecords. Defaults to None.
            filter_blank (list, optional): Exclude slides blank in these cols.
                Defaults to None.
            min_tiles (int, optional): Minimum number of tiles a slide must
                have to be included in evaluation. Defaults to 0.
            checkpoint (str, optional): Path to cp.ckpt file, if evaluating a
                saved checkpoint. Defaults to None.
            eval_k_fold (int, optional): K-fold iteration number to evaluate.
                Defaults to None. If None, will evaluate all tfrecords
                irrespective of K-fold.
            splits (str, optional): Filename of JSON file in which to log
                train/val splits. Looks for filename in project root directory.
                Defaults to "splits.json".
            max_tiles (int, optional): Maximum number of tiles from each slide
                to evaluate. Defaults to 0. If zero, will include all tiles.
            mixed_precision (bool, optional): Enable mixed precision.
                Defaults to True.
            allow_tf32 (bool): Allow internal use of Tensorfloat-32 format.
                Defaults to False.
            input_header (str, optional): Annotation column header to use as
                additional input. Defaults to None.
            load_method (str): Either 'full' or 'weights'. Method to use
                when loading a Tensorflow model. If 'full', loads the model with
                ``tf.keras.models.load_model()``. If 'weights', will read the
                ``params.json``configuration file, build the model architecture,
                and then load weights from the given model with
                ``Model.load_weights()``. Loading with 'full' may improve
                compatibility across Slideflow versions. Loading with 'weights'
                may improve compatibility across hardware & environments.
            save_predictions (bool or str, optional): Save tile, slide, and
                patient-level predictions at each evaluation. May be 'csv',
                'feather', or 'parquet'. If False, will not save predictions.
                Defaults to 'parquet'.
            custom_objects (dict, Optional): Dictionary mapping names
                (strings) to custom classes or functions. Defaults to None.
            **kwargs: Additional keyword arguments to the `Trainer.evaluate()`
                function.

        Returns:
            Dict: Dictionary of keras training results, nested by epoch.
        """
        log.info(f'Evaluating model at [green]{model}')
        trainer, eval_dts = self._prepare_trainer(
            model=model,
            dataset=dataset,
            outcomes=outcomes,
            checkpoint=checkpoint,
            eval_k_fold=eval_k_fold,
            splits=splits,
            max_tiles=max_tiles,
            input_header=input_header,
            mixed_precision=mixed_precision,
            allow_tf32=allow_tf32,
            load_method=load_method,
            custom_objects=custom_objects,
        )
        return trainer.evaluate(eval_dts, **kwargs)

    def evaluate_clam(
        self,
        exp_name: str,
        pt_files: str,
        outcomes: Union[str, List[str]],
        tile_px: int,
        tile_um: Union[int, str],
        *,
        k: int = 0,
        eval_tag: Optional[str] = None,
        filters: Optional[Dict] = None,
        filter_blank: Optional[Union[str, List[str]]] = None,
        attention_heatmaps: bool = True
    ) -> None:
        """Evaluate CLAM model on activations and export attention heatmaps.

        Args:
            exp_name (str): Name of experiment to evaluate (subfolder in clam/)
            pt_files (str): Path to pt_files containing tile-level features.
            outcomes (str or list): Annotation column that specifies labels.
            tile_px (int): Tile width in pixels.
            tile_um (int or str): Tile width in microns (int) or magnification
                (str, e.g. "20x").

        Keyword Args:
            k (int, optional): K-fold / split iteration to evaluate. Evaluates
                the model saved as s_{k}_checkpoint.pt. Defaults to 0.
            eval_tag (str, optional): Unique identifier for this evaluation.
                Defaults to None
            filters (dict, optional): Filters to use when selecting tfrecords.
                Defaults to None.
            filter_blank (list, optional): Exclude slides blank in these cols.
                Defaults to None.
            attention_heatmaps (bool, optional): Save attention heatmaps of
                validation dataset. Defaults to True.

        Returns:
            None
        """

        import slideflow.clam as clam
        from slideflow.clam.create_attention import export_attention
        from slideflow.clam.datasets.dataset_generic import Generic_MIL_Dataset

        # Detect source CLAM experiment which we are evaluating.
        # First, assume it lives in this project's clam folder
        if exists(join(self.root, 'clam', exp_name, 'experiment.json')):
            exp_name = join(self.root, 'clam', exp_name)
        elif exists(join(exp_name, 'experiment.json')):
            pass
        else:
            raise errors.CLAMError(f"Unable to find experiment '{exp_name}'")

        log.info(f'Loading experiment from [green]{exp_name}[/], k={k}')
        eval_dir = join(exp_name, 'eval')
        if not exists(eval_dir):
            os.makedirs(eval_dir)

        # Set up evaluation directory with unique evaluation tag
        existing_tags = [int(d) for d in os.listdir(eval_dir) if d.isdigit()]
        if eval_tag is None:
            eval_tag = '0' if not existing_tags else str(max(existing_tags))

        # Ensure evaluation tag will not overwrite existing results
        if eval_tag in existing_tags:
            unique, base_tag = 1, eval_tag
            eval_tag = f'{base_tag}_{unique}'
            while exists(join(eval_dir, eval_tag)):
                eval_tag = f'{base_tag}_{unique}'
                unique += 1
            log.info(f"Tag {base_tag} already exists, using tag 'eval_tag'")

        # Load trained model checkpoint
        ckpt_path = join(exp_name, 'results', f's_{k}_checkpoint.pt')
        eval_dir = join(eval_dir, eval_tag)
        if not exists(eval_dir):
            os.makedirs(eval_dir)
        args_dict = sf.util.load_json(join(exp_name, 'experiment.json'))
        args = SimpleNamespace(**args_dict)
        args.save_dir = eval_dir
        # Update any missing arguments with current defaults
        _default_args = clam.get_args()
        for _a in _default_args.__dict__:
            if not hasattr(args, _a):
                _default = getattr(_default_args, _a)
                log.info(f"Argument {_a} not found in CLAM model configuration "
                         f"file; using default value of {_default}.")
                setattr(args, _a, _default)

        dataset = self.dataset(
            tile_px=tile_px,
            tile_um=tile_um,
            filters=filters,
            filter_blank=filter_blank
        )
        slides = dataset.slides()
        eval_slides = [s for s in slides if exists(join(pt_files, s+'.pt'))]
        dataset = dataset.filter(filters={'slide': eval_slides})
        slide_labels, unique_labels = dataset.labels(outcomes, use_float=False)

        # Set up evaluation annotations file based off existing pt_files
        outcome_dict = dict(zip(range(len(unique_labels)), unique_labels))
        with open(join(eval_dir, 'eval_annotations.csv'), 'w') as eval_file:
            writer = csv.writer(eval_file)
            header = ['patient', 'slide', outcomes]
            writer.writerow(header)
            for slide in eval_slides:
                row = [slide, slide]
                row += [outcome_dict[slide_labels[slide]]]  # type: ignore
                writer.writerow(row)

        clam_dataset = Generic_MIL_Dataset(
            csv_path=join(eval_dir, 'eval_annotations.csv'),
            data_dir=pt_files,
            shuffle=False,
            seed=args.seed,
            print_info=True,
            label_col=outcomes,
            label_dict=dict(zip(unique_labels, range(len(unique_labels)))),
            patient_strat=False,
            ignore=[]
        )

        clam.evaluate(ckpt_path, args, clam_dataset)

        # Get attention from trained model on validation set
        attention_tfrecords = dataset.tfrecords()
        attention_dir = join(eval_dir, 'attention')
        if not exists(attention_dir):
            os.makedirs(attention_dir)
        reverse_labels = dict(zip(range(len(unique_labels)), unique_labels))
        export_attention(
            args_dict,
            ckpt_path=ckpt_path,
            outdir=attention_dir,
            pt_files=pt_files,
            slides=dataset.slides(),
            reverse_labels=reverse_labels,
            labels=slide_labels
        )
        if attention_heatmaps:
            heatmaps_dir = join(eval_dir, 'attention_heatmaps')
            if not exists(heatmaps_dir):
                os.makedirs(heatmaps_dir)

            for tfr in attention_tfrecords:
                attention_dict = {}
                slide = path_to_name(tfr)
                try:
                    with open(join(attention_dir, slide+'.csv'), 'r') as f:
                        reader = csv.reader(f)
                        for row in reader:
                            attention_dict.update({int(row[0]): float(row[1])})
                except FileNotFoundError:
                    print(f'No attention scores for slide {slide}, skipping')
                    continue
                dataset.tfrecord_heatmap(
                    tfr,
                    tile_dict=attention_dict,
                    outdir=heatmaps_dir
                )

    def extract_tiles(
        self,
        tile_px: int,
        tile_um: Union[int, str],
        *,
        filters: Optional[Dict] = None,
        filter_blank: Optional[Union[str, List[str]]] = None,
        **kwargs: Any
    ) -> None:
        """Extracts tiles from slides. Preferred use is calling
        :func:`slideflow.dataset.Dataset.extract_tiles` on a
        :class:`slideflow.dataset.Dataset` directly.

        Args:
            tile_px (int): Size of tiles to extract, in pixels.
            tile_um (int or str): Size of tiles to extract, in microns (int) or
                magnification (str, e.g. "20x").

        Keyword Args:
            save_tiles (bool, optional): Save tile images in loose format.
                Defaults to False.
            save_tfrecords (bool, optional): Save tile images as TFRecords.
                Defaults to True.
            source (str, optional): Process slides only from this source.
                Defaults to None (all slides in project).
            stride_div (int, optional): Stride divisor. Defaults to 1.
                A stride of 1 will extract non-overlapping tiles.
                A stride_div of 2 will extract overlapping tiles with a stride
                equal to 50% of the tile width.
            enable_downsample (bool, optional): Enable downsampling when
                reading slides. Defaults to True. This may result in corrupted
                image tiles if downsampled slide layers are corrupted or
                incomplete. Recommend manual confirmation of tile integrity.
            roi_method (str): Either 'inside', 'outside', 'auto', or 'ignore'.
                Determines how ROIs are used to extract tiles.
                If 'inside' or 'outside', will extract tiles in/out of an ROI,
                and skip the slide if an ROI is not available.
                If 'auto', will extract tiles inside an ROI if available,
                and across the whole-slide if no ROI is found.
                If 'ignore', will extract tiles across the whole-slide
                regardless of whether an ROI is available.
                Defaults to 'auto'.
            skip_extracted (bool, optional): Skip already extracted slides.
                Defaults to True.
            tma (bool, optional): Reads slides as Tumor Micro-Arrays (TMAs),
                detecting and extracting tumor cores. Defaults to False.
            randomize_origin (bool, optional): Randomize pixel starting
                position during extraction. Defaults to False.
            buffer (str, optional): Copy slides here before extraction.
                Improves processing speed if using an SSD/ramdisk buffer.
                Defaults to None.
            num_workers (int, optional): Extract tiles from this many slides
                simultaneously. Defaults to 1.
            q_size (int, optional): Queue size for buffer. Defaults to 4.
            qc (str, optional): 'otsu', 'blur', 'both', or None. Perform blur
                detection quality control - discarding tiles with detected
                out-of-focus regions or artifact - and/or otsu's method.
                Defaults to None.
            report (bool, optional): Save a PDF report of tile extraction.
                Defaults to True.
            normalizer (str, optional): Normalization strategy.
                Defaults to None.
            normalizer_source (str, optional): Path to normalizer source image.
                Defaults to None (use internal image at slide.norm_tile.jpg).
            whitespace_fraction (float, optional): Range 0-1. Defaults to 1.
                Discard tiles with this fraction of whitespace. If 1, will not
                perform whitespace filtering.
            whitespace_threshold (int, optional): Range 0-255. Threshold above
                which a pixel (RGB average) is considered whitespace.
                Defaults to 230.
            grayspace_fraction (float, optional): Range 0-1. Discard tiles with
                this fraction of grayspace. If 1, will not perform grayspace
                filtering. Defaults to 0.6.
            grayspace_threshold (float, optional): Range 0-1. Pixels in HSV
                format with saturation below this are considered grayspace.
                Defaults to 0.05.
            img_format (str, optional): 'png' or 'jpg'. Defaults to 'jpg'.
                Image format to use in tfrecords. PNG (lossless) for
                fidelity, JPG (lossy) for efficiency.
            full_core (bool, optional): Only used if extracting from TMA. Save
                entire TMA core as image. Otherwise, will extract sub-images
                from each core at the tile micron size. Defaults to False.
            shuffle (bool, optional): Shuffle tiles before tfrecords storage.
                Defaults to True.
            num_threads (int, optional): Threads for each tile extractor.
                Defaults to 4.
            qc_blur_radius (int, optional): Blur radius for out-of-focus area
                detection. Used if qc=True. Defaults to 3.
            qc_blur_threshold (float, optional): Blur threshold for detecting
                out-of-focus areas. Used if qc=True. Defaults to 0.1.
            qc_filter_threshold (float, optional): Float between 0-1.
                Tiles with more than this proportion of blur will be discarded.
                Used if qc=True. Defaults to 0.6.
            qc_mpp (float, optional): Microns-per-pixel indicating image
                magnification level at which quality control is performed.
                Defaults to mpp=4 (effective magnification 2.5 X)
            dry_run (bool, optional): Determine tiles that would be extracted,
                but do not export any images. Defaults to None.
            max_tiles (int, optional): Only extract this many tiles per slide.
                Defaults to None.

        Returns:
            Dictionary mapping slide paths to each slide's SlideReport
            (:class:`slideflow.slide.report.SlideReport`)
        """
        dataset = self.dataset(
            tile_px,
            tile_um,
            filters=filters,
            filter_blank=filter_blank,
            verification='slides'
        )
        dataset.extract_tiles(**kwargs)

    def gan_train(
        self,
        dataset: Dataset,
        *,
        model: str = 'stylegan3',
        outcomes: Optional[Union[str, List[str]]] = None,
        exp_label: Optional[str] = None,
        mirror: bool = True,
        metrics: Optional[Union[str, List[str]]] = None,
        dry_run: bool = False,
        **kwargs
    ) -> None:
        """Train a GAN network.

        Args:
            dataset (:class:`slideflow.Dataset`): Training dataset.

        Keyword Args:
            allow_tf32 (bool): Allow internal use of Tensorflow-32.
                Option only available for StyleGAN2. Defaults to True.
            aug (str): Augmentation mode. Options include 'ada',
                'noaug', 'fixed'. Defaults to 'ada'.
            augpipe (str): Augmentation pipeline. Options include
                'blit', 'geom', 'color', 'filter', 'noise', 'cutout', 'bg',
                'bgc', 'bgcfnc'. Only available for StyleGAN2.
                Defaults to 'bgcfnc'.
            batch (int, optional): Override batch size set by `cfg`.
            cfg (str): StyleGAN2 base configuration. Options include
                'auto', 'stylegan2', 'paper256', 'paper512', 'paper1024', and
                'cifar'. Defaults to 'auto'.
            dry_run (bool): Set up training but do not execute.
                Defaults to False.
            exp_label (str, optional): Experiment label. Defaults to None.
            freezed (int): Freeze this many discriminator layers.
                Defaults to 0.
            fp32 (bool, optional): Disable mixed-precision training. Defaults
                to False.
            gamma (float, optional): Override R1 gamma from configuration
                (set with `cfg`).
            gpus (int): Number GPUs to train on in parallel. Defaults
                to 1.
            kimg (int): Override training duration in kimg (thousand
                images) set by `cfg`. Most configurations default to 25,000
                kimg (25 million images).
            lazy_resume (bool). Allow lazy loading from saved pretrained
                networks, for example to load a non-conditional network
                when training a conditional network. Defaults to False.
            mirror (bool): Randomly flip/rotate images during
                training. Defaults to True.
            metrics (str, list(str), optional): Metrics to calculate during
                training. Options include 'fid50k', 'is50k', 'ppl_zfull',
                'ppl_wfull', 'ppl_zend', 'ppl2_wend', 'ls', and 'pr50k3'.
                Defaults to None.
            model (str): Architecture to train. Only currently valid model
                architecture is "stylegan2". Defaults to "stylegan2".
            nhwc (bool): Use NWHC memory format with FP16. Defaults to False.
            nobench (bool): Disable cuDNN benchmarking. Defaults to False.
            outcomes (str, list(str), optional): Class conditioning outcome
                labels for training a class-conditioned GAN. If not provided,
                trains an unconditioned GAN. Defaults to None.
            resume (str): Load previous network. Options include
                'noresume' , 'ffhq256', 'ffhq512', 'ffhqq1024', 'celebahq256',
                'lsundog256', <file>, or <url>. Defaults to 'noresume'.
            snap (int): Snapshot interval for saving network and
                example images. Defaults to 50 ticks.

        Examples
            Train StyleGAN2 from a Slideflow dataset.

                >>> P = sf.Project('/project/path')
                >>> dataset = P.dataset(tile_px=512, tile_um=400)
                >>> P.gan_train(dataset=dataset, exp_label="MyExperiment", ...)

            Train StyleGAN2 as a class-conditional network.

                >>> P.gan_train(..., outcomes='class_label')

            Train using a pretrained network.

                >>> P.gan_train(..., resume='/path/to/network.pkl')

            Train with multiple GPUs.

                >>> P.gan_train(..., gpus=4)
        """
        # Validate the method and import the appropriate submodule
        supported_models = ('stylegan2', 'stylegan3')
        if model not in supported_models:
            raise ValueError(f"Unknown method '{model}'. Valid methods "
                             f"include: {', '.join(supported_models)}")
        if model == 'stylegan2':
            from slideflow.gan.stylegan2 import stylegan2 as network
        elif model == 'stylegan3':
            from slideflow.gan.stylegan3 import stylegan3 as network  # type: ignore
        if metrics is not None:
            log.warn(
                "StyleGAN2 metrics are not fully implemented for Slideflow."
            )

        # Setup directories
        gan_root = join(self.root, 'gan')
        if not exists(gan_root):
            os.makedirs(gan_root)
        if exp_label is None:
            exp_label = 'gan_experiment'
        gan_dir = sf.util.get_new_model_dir(gan_root, exp_label)

        # Write GAN configuration
        config_loc = join(gan_dir, 'slideflow_config.json')
        sf.util.write_json(dict(
            project_path=self.root,
            tile_px=dataset.tile_px,
            tile_um=dataset.tile_um,
            model_type='categorical',
            outcome_label_headers=outcomes,
            filters=dataset._filters,
            filter_blank=dataset._filter_blank,
        ), config_loc)

        # Train the GAN
        network.train.train(
            ctx=None,
            outdir=gan_dir,
            dry_run=dry_run,
            slideflow=config_loc,
            cond=(outcomes is not None),
            mirror=mirror,
            metrics=metrics,
            **kwargs)

    def gan_generate(
        self,
        network_pkl: str,
        out: str,
        seeds: List[int],
        **kwargs
    ) -> None:
        """Generate images from a trained GAN network.

        Args:
            network_pkl (str): Path to a trained StyleGAN2 network (``.pkl``)
            out (str): Directory in which to save generated images.
            seeds (list(int)): Seeds for which images will be generated.

        Keyword args:
            format (str, optional): Image format, either 'jpg' or 'png'.
                Defaults to 'png'.
            truncation_psi (float, optional): Truncation PSI. Defaults to 1.
            noise_mode (str, optional): Either 'const', 'random', or 'none'.
                Defaults to 'const'.
            class_idx (int, optional): Class index to generate, for class-
                conditional networks. Defaults to None.
            save_projection (bool, optional): Save weight projection for each
                generated image as an `.npz` file in the out directory.
                Defaults to False.
            resize (bool, optional): Crop/resize images to a target micron/pixel
                size. Defaults to False.
            gan_um (int, optional): Size of GAN images in microns. Used for
                cropping/resizing images to a target size. Defaults to None.
            gan_px (int, optional): Size of GAN images in pixels. Used for
                cropping/resizing images to a target size. Defaults to None.
            target_um (int, optional): Crop/resize GAN images to this micron
                size. Defaults to None.
            target_px (int, optional): Crop/resize GAN images to this pixel
                size. Defaults to None.

        Examples
            Save images as ``.png`` for seeds 0-100.

                >>> network_pkl = '/path/to/trained/gan.pkl'
                >>> P.gan_generate(
                ...     network_pkl,
                ...     out='/dir',
                ...     format='jpg',
                ...     seeds=range(100))

            Save images in TFRecord format.

                >>> P.gan_generate(... out='target.tfrecords')

            Save images of class '0' for a class-conditional GAN.

                >>> P.gan_generate(..., class_idx=0)

            Resize GAN images (trained at 512 px / 400 um) to match a target
            tile size (299 px / 302 um).

                >>> P.gan_generate(
                ...     ...,
                ...     gan_px=512,
                ...     gan_um=400,
                ...     target_px=299,
                ...     target_um=302)
        """
        from slideflow.gan.stylegan2 import stylegan2

        stylegan2.generate.generate_images(
            network_pkl,
            outdir=out,
            seeds=seeds,
            **kwargs
        )

    @auto_dataset
    def generate_features(
        self,
        model: str,
        *,
        dataset: Dataset,
        filters: Optional[Dict] = None,
        filter_blank: Optional[Union[str, List[str]]] = None,
        min_tiles: int = 0,
        max_tiles: int = 0,
        outcomes: Optional[List[str]] = None,
        torch_export: Optional[str] = None,
        **kwargs: Any
    ) -> sf.DatasetFeatures:
        """Calculate layer features / activations.

        Args:
            model (str): Path to model

        Keyword Args:
            dataset (:class:`slideflow.dataset.Dataset`, optional): Dataset
                from which to generate activations. If not supplied, calculate
                activations for all tfrecords compatible with the model,
                optionally using provided filters and filter_blank.
            filters (dict, optional): Filters to use when selecting tfrecords.
                 Defaults to None.
            filter_blank (list, optional): Slides blank in these columns will
                be excluded. Defaults to None.
            min_tiles (int, optional): Only include slides with this minimum
                number of tiles. Defaults to 0.
            max_tiles (int, optional): Only include maximum of this many tiles
                per slide. Defaults to 0 (all tiles).
            outcomes (list, optional): Column header(s) in annotations file.
                Used for category-level comparisons. Defaults to None.
            torch_export (str, optional): Path. Export activations to
                torch-compatible file at this location. Defaults to None.
            layers (list(str)): Layers from which to generate activations.
                Defaults to 'postconv'.
            export (str): Path to CSV file. Save activations in CSV format.
                Defaults to None.
            cache (str): Path to PKL file. Cache activations at this location.
                Defaults to None.
            include_logits (bool): Generate and store logit predictions along
                with layer activations. Defaults to True.
            batch_size (int): Batch size to use when calculating activations.
                Defaults to 32.

        Returns:
            :class:`slideflow.DatasetFeatures`
        """
        # Prepare dataset and annotations
        dataset = dataset.clip(max_tiles)
        if outcomes is not None:
            labels = dataset.labels(outcomes, format='name')[0]
        else:
            labels = None
        df = sf.DatasetFeatures(model=model,
                                dataset=dataset,
                                annotations=labels,
                                **kwargs)
        if torch_export:
            df.to_torch(torch_export)
        return df

    def generate_features_for_clam(
        self,
        model: str,
        outdir: str = 'auto',
        dataset: Optional[Dataset] = None,
        layers: Union[str, List[str]] = 'postconv',
        force_regenerate: bool = False,
        min_tiles: int = 16
    ) -> str:
        """Generate tile-level features for slides for use with CLAM.

        Args:
            model (str): Path to model from which to generate activations.
                May provide either this or "pt_files"
            outdir (str, optional): Save exported activations in .pt format.
                Defaults to 'auto' (project directory).

        Keyword Args:
            dataset (:class:`slideflow.dataset.Dataset`, optional): Dataset
                from which to generate activations. If not supplied, calculate
                activations for all tfrecords compatible with the model,
                optionally using provided filters and filter_blank.
            min_tiles (int, optional): Minimum tiles per slide. Skip slides
                not meeting this threshold. Defaults to 8.
            filters (dict, optional): Filters to use when selecting tfrecords.
                Defaults to None.
            filter_blank (list, optional): Slides blank in these columns will
                be excluded. Defaults to None.
            layers (list, optional): Which model layer(s) generate activations.
                Defaults to 'postconv'.
            max_tiles (int, optional): Maximum tiles to take per slide.
                Defaults to 0.
            force_regenerate (bool, optional): Forcibly regenerate activations
                for all slides even if .pt file exists. Defaults to False.

        Returns:
            Path to directory containing exported .pt files
        """

        # Check if the model exists and has a valid parameters file
        if exists(model):
            config = sf.util.get_model_config(model)

            if dataset is None:
                log.debug(f"Auto-building dataset from provided model {model}")
                dataset = self.dataset(
                    tile_px=config['tile_px'],
                    tile_um=config['tile_um'],
                    min_tiles=min_tiles
                )

            # Set up the pt_files directory for storing model activations
            if outdir.lower() == 'auto':
                if 'k_fold_i' in config:
                    _end = f"_kfold{config['k_fold_i']}"
                else:
                    _end = ''
                outdir = join(self.root, 'pt_files', config['model_name'] + _end)
        elif dataset is None:
            raise ValueError(
                "Must supply 'dataset' if generating features from an "
                "Imagenet-pretrained model."
            )

        # Verify the dataset min tiles is at least 8
        if dataset.min_tiles < 8:
            raise ValueError(
                "Slides must have at >=8 tiles to train CLAM (provided "
                f"dataset has min_tiles={dataset.min_tiles})"
            )

        # If the model does not exist, check if it is an architecture name
        # (for using an Imagenet pretrained model)
        if model in sf.ModelParams.ModelDict:
            log.info(f"Generating features from Imagenet-pretrained {model}.")
            _hp = sf.ModelParams(
                tile_px=dataset.tile_px,
                tile_um=dataset.tile_um,
                model=model,
                include_top=False,
                hidden_layers=0
            )

            # Set the pt_files directory if not provided
            if outdir.lower() == 'auto':
                outdir = join(self.root, 'pt_files', model)

            # Now, overwrite the model name with the built model
            model = _hp.build_model(
                num_classes=1,
                pretrain='imagenet'
            )  # type: ignore

            if sf.backend() == 'torch':
                import torch
                model = model.to(torch.device('cuda'))  # type: ignore
                model.eval()  # type: ignore
        elif not exists(model):
            raise ValueError(
                f"'{model}' is neither a path to a saved model nor the name "
                "of a valid model architecture.")

        # Create the pt_files directory
        if not exists(outdir):
            os.makedirs(outdir)

        # Detect already generated pt files
        done = [
            path_to_name(f) for f in os.listdir(outdir)
            if sf.util.path_to_ext(join(outdir, f)) == 'pt'
        ]

        if not force_regenerate and len(done):
            all_slides = dataset.slides()
            slides_to_generate = [s for s in all_slides if s not in done]
            if len(slides_to_generate) != len(all_slides):
                to_skip = len(all_slides) - len(slides_to_generate)
                skip_p = f'{to_skip}/{len(all_slides)}'
                log.info(f"Skipping {skip_p} finished slides.")
            if not slides_to_generate:
                log.warn("No slides to generate CLAM features.")
                return outdir
            dataset = dataset.filter(filters={'slide': slides_to_generate})
            filtered_slides_to_generate = dataset.slides()
            log.info(f'Skipping {len(done)} files already done.')
            log.info(f'Working on {len(filtered_slides_to_generate)} slides')

        # Set up activations interface
        df = sf.DatasetFeatures(
            model=model,
            dataset=dataset,
            layers=layers,
            include_logits=False,
        )
        df.to_torch(outdir)
        return outdir

    @auto_dataset
    def generate_heatmaps(
        self,
        model: str,
        *,
        dataset: Dataset,
        filters: Optional[Dict] = None,
        filter_blank: Optional[Union[str, List[str]]] = None,
        min_tiles: int = 0,
        outdir: Optional[str] = None,
        resolution: str = 'low',
        batch_size: int = 32,
        roi_method: str = 'auto',
        num_threads: Optional[int] = None,
        img_format: str = 'auto',
        skip_completed: bool = False,
        verbose: bool = True,
        **kwargs: Any
    ) -> None:
        """Creates predictive heatmap overlays on a set of slides.

        Args:
            model (str): Path to Tensorflow model.

        Keyword Args:
            dataset (:class:`slideflow.dataset.Dataset`, optional): Dataset
                from which to generate predictions. If not supplied, will
                generate predictions for all project tfrecords at the
                tile_px/tile_um matching the model, optionally using provided
                filters and filter_blank.
            filters (dict, optional): Filters to use when selecting tfrecords.
                Defaults to None.
            filter_blank (list, optional): Exclude slides blank in these cols.
                Defaults to None.
            min_tiles (int, optional): Minimum tiles per slide. Skip slides
                not meeting this threshold. Defaults to 8.
            outdir (path, optional): Directory in which to save heatmap images.
            resolution (str, optional): Heatmap resolution. Defaults to 'low'.
                "low" uses a stride equal to tile width.
                "medium" uses a stride equal 1/2 tile width.
                "high" uses a stride equal to 1/4 tile width.
            batch_size (int, optional): Batch size during heatmap calculation.
                Defaults to 64.
            roi_method (str): Either 'inside', 'outside', 'auto', or 'ignore'.
                Determines how ROIs are used to extract tiles.
                If 'inside' or 'outside', will extract tiles in/out of an ROI,
                and raise errors.MissingROIError if an ROI is not available.
                If 'auto', will extract tiles inside an ROI if available,
                and across the whole-slide if no ROI is found.
                If 'ignore', will extract tiles across the whole-slide
                regardless of whether an ROI is available.
                Defaults to 'auto'.
            num_threads (int, optional): Number of threads for tile extraction.
                Defaults to CPU core count.
            img_format (str, optional): Image format (png, jpg) to use when
                extracting tiles from slide. Must match the image format
                the model was trained on. If 'auto', will use the format
                logged in the model params.json.
            skip_completed (bool, optional): Skip heatmaps for slides that
                already have heatmaps in target directory.
            show_roi (bool): Show ROI on heatmaps.
            interpolation (str): Interpolation strategy for predictions.
                Defaults to None.
                Includes all matplotlib imshow interpolation options.
            logit_cmap: Function or a dict used to create heatmap colormap.
                If None (default), separate heatmaps are generated for each
                category, with color representing category prediction.
                Each image tile will generate a list of preds of length O,
                If logit_cmap is a function, then the logit predictions will
                be passed, where O is the number of label categories.
                and the function is expected to return [R, G, B] values.
                If the logit_cmap is a dictionary, it should map 'r', 'g', and
                'b' to label indices; the prediction for these label categories
                will be mapped to corresponding colors. Thus, the corresponding
                color will only reflect predictions of up to three labels.
                Example (this would map predictions for label 0 to red, 3 to
                green, etc): {'r': 0, 'g': 3, 'b': 1 }
            verbose (bool): Show verbose output. Defaults to True.
            vmin (float): Minimimum value to display on heatmap. Defaults to 0.
            vcenter (float): Center value for color display on heatmap.
                Defaults to 0.5.
            vmax (float): Maximum value to display on heatmap. Defaults to 1.
        """

        # Prepare arguments for subprocess
        args = SimpleNamespace(**locals())
        del args.self

        # Prepare dataset
        config = sf.util.get_model_config(model)
        args.rois = dataset.rois()

        # Set resolution / stride
        resolutions = {'low': 1, 'medium': 2, 'high': 4}
        try:
            stride_div = resolutions[resolution]
        except KeyError:
            raise ValueError(f"Invalid resolution '{resolution}'.")
        args.stride_div = stride_div
        args.verbosity = self.verbosity  # Set logging level in subprocess
        args.img_format = img_format

        # Attempt to auto-detect supplied model name
        model_name = os.path.basename(model)
        if 'model_name' in config:
            model_name = config['model_name']

        # Make output directory
        outdir = outdir if outdir else join(self.root, 'heatmaps', model_name)
        if not exists(outdir):
            os.makedirs(outdir)
        args.outdir = outdir

        # Verbose output
        if verbose:
            n_poss_slides = len(dataset.slides())
            n_slides = len(dataset.slide_paths())
            log.info("Generating heatmaps for {} slides.".format(n_slides))
            log.info("Model: [green]{}".format(model))
            log.info("Tile px: {}".format(config['tile_px']))
            log.info("Tile um: {}".format(config['tile_um']))

        # Any function loading a slide must be kept in an isolated process,
        # as loading >1 slide in a single process causes instability.
        # I suspect this is a libvips or openslide issue but I haven't been
        # able to identify the root cause. Isolating processes when multiple
        # slides are to be processed sequentially is a functional workaround.
        for slide in dataset.slide_paths():
            name = path_to_name(slide)
            if (skip_completed and exists(join(outdir, f'{name}-custom.png'))):
                log.info(f'Skipping completed heatmap for slide {name}')
                return

            ctx = multiprocessing.get_context('spawn')
            process = ctx.Process(target=project_utils._heatmap_worker,
                                  args=(slide, args, kwargs))
            process.start()
            process.join()

    def generate_mosaic(
        self,
        df: "DatasetFeatures",
        dataset: Optional[Dataset] = None,
        *,
        filters: Optional[Dict] = None,
        filter_blank: Optional[Union[str, List[str]]] = None,
        outcomes: Optional[Union[str, List[str]]] = None,
        map_slide: Optional[str] = None,
        show_prediction: Optional[Union[int, str]] = None,
        predict_on_axes: Optional[List[int]] = None,
        max_tiles: int = 0,
        umap_cache: Optional[str] = None,
        use_float: bool = False,
        low_memory: bool = False,
        use_norm: bool = True,
        umap_kwargs: Dict = {},
        **kwargs: Any
    ) -> sf.Mosaic:
        """Generates a mosaic map by overlaying images onto mapped tiles.
            Image tiles are extracted from the provided set of TFRecords, and
            predictions + features from layer activations are calculated using
            the specified model. Tiles are mapped either with UMAP of layer
            activations (default behavior), or by using outcome predictions for
            two categories, mapped to X- and Y-axis (via predict_on_axes).

        Args:
            df (:class:`slideflow.DatasetFeatures`): Dataset.
            dataset (:class:`slideflow.dataset.Dataset`, optional): Dataset
                from which to generate mosaic. If not supplied, will generate
                mosaic for all tfrecords at the tile_px/tile_um matching
                the supplied model, optionally using filters/filter_blank.

        Keyword Args:
            filters (dict, optional): Filters dict to use when selecting
                tfrecords. Defaults to None.
            filter_blank (list, optional): Slides blank in these columns will
                be excluded. Defaults to None.
            outcomes (list, optional): Column name in annotations file from
                which to read category labels.
            map_slide (str, optional): None (default), 'centroid' or 'average'.
                If provided, will map slides using slide-level calculations,
                either mapping centroid tiles if 'centroid', or calculating
                node averages across tiles in a slide and mapping slide-level
                node averages, if 'average'.
            show_prediction (int or str, optional): May be either int or str,
                corresponding to label category. Predictions for this category
                will be displayed on the exported UMAP plot.
            max_tiles (int, optional): Limits tiles taken from each slide.
                Defaults to 0.
            umap_cache (str, optional): Path to PKL file in which to save/cache
                UMAP coordinates. Defaults to None.
            use_float (bool, optional): Interpret labels as continuous instead
                of categorical. Defaults to False.
            umap_kwargs (dict, optional): Dictionary of keyword arguments to
                pass to the UMAP function.
            low_memory (bool, optional): Limit memory during UMAP calculations.
                Defaults to False.
            use_norm (bool, optional): Display image tiles using the normalizer
                used during model training (if applicable). Detected from
                a model's metadata file (params.json). Defaults to True.
            figsize (Tuple[int, int], optional): Figure size. Defaults to
                (200, 200).
            num_tiles_x (int): Specifies the size of the mosaic map grid.
            expanded (bool): Controls tile assignment on grid spaces.
                If False, tile assignment is strict.
                If True, allows displaying nearby tiles if a grid is empty.
                Defaults to False.
            leniency (float): UMAP leniency. Defaults to 1.5.

        Returns:
            :class:`slideflow.Mosaic`: Mosaic object.
        """

        # Set up paths
        stats_root = join(self.root, 'stats')
        mosaic_root = join(self.root, 'mosaic')
        if not exists(stats_root):
            os.makedirs(stats_root)
        if not exists(mosaic_root):
            os.makedirs(mosaic_root)

        # Prepare dataset & model
        if isinstance(df.model, str):
            config = sf.util.get_model_config(df.model)
        else:
            raise ValueError(
                "Unable to auto-create Mosaic from DatasetFeatures created "
                "from a loaded Tensorflow/PyTorch model. Please use a "
                "DatasetFeatures object created from a saved Slideflow model, "
                "or manually create a mosaic with `sf.Mosaic`.")
        if dataset is None:
            tile_px, tile_um = config['hp']['tile_px'], config['hp']['tile_um']
            dataset = self.dataset(tile_px=tile_px, tile_um=tile_um)
        else:
            dataset._assert_size_matches_hp(config['hp'])
            tile_px = dataset.tile_px

        # Filter and clip dataset
        dataset = dataset.filter(filters=filters, filter_blank=filter_blank)
        dataset = dataset.clip(max_tiles)

        # Get TFrecords, and prepare a list for focus, if requested
        tfr = dataset.tfrecords()
        n_slides = len([t for t in tfr if path_to_name(t) in df.slides])
        log.info(f'Generating mosaic from {n_slides} slides')

        # If a header category is supplied and we are not showing predictions,
        # then assign slide labels from annotations
        model_type = config['model_type']
        if model_type == 'linear':
            use_float = True
        if outcomes and (show_prediction is None):
            labels, _ = dataset.labels(outcomes,
                                       use_float=use_float,
                                       format='name')
        else:
            labels = {}  # type: ignore

        # If showing predictions, try to automatically load prediction labels
        if (show_prediction is not None) and (not use_float):
            outcome_labels = config['outcome_labels']
            model_type = model_type if model_type else config['model_type']
            log.info(f'Loaded pred labels found at [green]{df.model}')

        # Create mosaic map from UMAP of layer activations
        umap = sf.SlideMap.from_features(
            df,
            map_slide=map_slide,
            cache=umap_cache,
            low_memory=low_memory,
            **umap_kwargs
        )
        # If displaying centroid AND predictions, show slide-level predictions
        # rather than tile-level predictions
        if (map_slide == 'centroid') and show_prediction is not None:
            log.info('Showing slide-level predictions at point of centroid')

            # If not model has not been assigned, assume categorical model
            model_type = model_type if model_type else 'categorical'

            # Get predictions
            if model_type == 'categorical':
                s_pred = df.logits_predict()
                s_perc = df.logits_percent()
            else:
                s_pred = s_perc = df.logits_mean()  # type: ignore

            # If show_prediction is provided (either a number or string),
            # then display ONLY the prediction for the provided category
            if type(show_prediction) == int:
                log.info(f'Showing preds for {show_prediction} as colormap')
                labels = {
                    k: v[show_prediction] for k, v in s_perc.items()
                }
                show_prediction = None
            elif type(show_prediction) == str:
                log.info(f'Showing preds for {show_prediction} as colormap')
                reversed_labels = {v: k for k, v in outcome_labels.items()}
                if show_prediction not in reversed_labels:
                    raise ValueError(f"Unknown category '{show_prediction}'")
                labels = {
                    k: v[int(reversed_labels[show_prediction])]
                    for k, v in s_perc.items()
                }
                show_prediction = None
            elif use_float:
                # Displaying linear predictions needs to be implemented here
                raise NotImplementedError(
                    "Showing slide preds not supported for linear outcomes."
                )
            # Otherwise, show_prediction is assumed to be just "True",
            # in which case show categorical predictions
            else:
                try:
                    labels = {
                        k: outcome_labels[v] for k, v in s_pred.items()
                    }
                except KeyError:
                    # Try interpreting prediction label keys as strings
                    labels = {
                        k: outcome_labels[str(v)] for k, v in s_pred.items()
                    }

        if labels:
            umap.label_by_slide(labels)
        if show_prediction and (map_slide != 'centroid'):
            umap.label('predictions', translate=outcome_labels)
        umap.filter(dataset.slides())

        mosaic = sf.Mosaic(
            umap,
            dataset.tfrecords(),
            normalizer=(df.normalizer if use_norm else None),
            **kwargs
        )
        return mosaic

    def generate_mosaic_from_annotations(
        self,
        header_x: str,
        header_y: str,
        *,
        dataset: Dataset,
        model: Optional[str] = None,
        outcomes: Optional[Union[str, List[str]]] = None,
        max_tiles: int = 100,
        use_optimal_tile: bool = False,
        cache: Optional[str] = None,
        batch_size: int = 32,
        **kwargs: Any
    ) -> sf.Mosaic:
        """Generates mosaic map by overlaying images onto mapped tiles.
            Slides are mapped with slide-level annotations, x-axis determined
            from header_x, y-axis from header_y. If use_optimal_tile is False
            and no model is provided, tje first image tile in each TFRecord
            will be displayed. If optimal_tile is True, layer
            activations for all tiles in each slide are calculated using the
            provided model, and the tile nearest to centroid is used.

        Args:
            header_x (str): Annotations file header with X-axis coords.
            header_y (str): Annotations file header with Y-axis coords.

        Keyword Args:
            dataset (:class:`slideflow.dataset.Dataset`): Dataset object.
            model (str, optional): Path to Tensorflow model to use when
                generating layer activations.
            Defaults to None.
                If not provided, mosaic will not be calculated or saved.
                If provided, saved in project mosaic directory.
            outcomes (list(str)): Column name(s) in annotations file from which
                to read category labels.
            max_tiles (int, optional): Limits the number of tiles taken from
                each slide. Defaults to 0.
            use_optimal_tile (bool, optional): Use model to calculate layer
                activations for all tiles in each slide, and choosing tile
                nearest centroid for each slide for display.
            cache (str, optional): Path to PKL file to cache node
                activations. Defaults to None.
            batch_size (int, optional): Batch size for model. Defaults to 64.
            figsize (Tuple[int, int], optional): Figure size. Defaults to
                (200, 200).
            num_tiles_x (int): Specifies the size of the mosaic map grid.
            expanded (bool): Controls tile assignment on grid spaces.
                If False, tile assignment is strict.
                If True, allows displaying nearby tiles if a grid is empty.
                Defaults to False.
            leniency (float): UMAP leniency. Defaults to 1.5.
        """

        # Setup paths
        stats_root = join(self.root, 'stats')
        mosaic_root = join(self.root, 'mosaic')
        if not exists(stats_root):
            os.makedirs(stats_root)
        if not exists(mosaic_root):
            os.makedirs(mosaic_root)

        # Filter dataset to exclude slides blank in the x and y header columns
        dataset = dataset.filter(filter_blank=[header_x, header_y])
        dataset = dataset.clip(max_tiles)

        # We are assembling a list of slides from the TFRecords path list,
        # because we only want to use slides that have a corresponding TFRecord
        # (some slides did not have a large enough ROI for tile extraction
        # & some slides may be in the annotations but are missing a slide)
        slides = [path_to_name(tfr) for tfr in dataset.tfrecords()]
        labels, _ = dataset.labels([header_x, header_y], use_float=True)
        umap_x = np.array([labels[slide][0]  # type: ignore
                           for slide in slides])
        umap_y = np.array([labels[slide][1]  # type: ignore
                           for slide in slides])

        if use_optimal_tile and model is None:
            raise ValueError("Optimal tile calculation requires a model.")
        elif use_optimal_tile:
            # Calculate most representative tile in each TFRecord for display
            assert model is not None
            df = sf.DatasetFeatures(model=model,
                                    dataset=dataset,
                                    batch_size=batch_size,
                                    cache=cache)
            opt_ind, _ = sf.stats.calculate_centroid(df.activations)

            # Restrict mosaic to only slides that had enough tiles to
            # calculate an optimal index from centroid
            success_slides = list(opt_ind.keys())
            sf.util.multi_warn(
                slides,
                lambda x: x not in success_slides,
                'Unable to calculate optimal tile for {}, skipping'
            )
            umap_x = np.array([
                labels[slide][0]  # type: ignore
                for slide in success_slides
            ])
            umap_y = np.array([
                labels[slide][1]  # type: ignore
                for slide in success_slides
            ])
            umap_slides = np.array(success_slides)
            umap_tfr_idx = np.array([
                opt_ind[slide] for slide in success_slides
            ])
        else:
            # Take the first tile from each slide/TFRecord
            umap_slides = np.array(slides)
            umap_tfr_idx = np.zeros(len(slides))

        umap = sf.SlideMap.from_precalculated(
            x=umap_x,
            y=umap_y,
            slides=umap_slides,
            tfr_index=umap_tfr_idx,
        )
        if outcomes is not None:
            slide_to_category, _ = dataset.labels(outcomes, format='name')
            umap.label_by_slide(slide_to_category)

        mosaic = sf.Mosaic(
            umap,
            dataset.tfrecords(),
            tile_select='centroid' if use_optimal_tile else 'nearest',
            **kwargs
        )
        return mosaic

    def generate_thumbnails(
        self,
        size: int = 512,
        *,
        dataset: Optional[Dataset] = None,
        filters: Optional[Dict] = None,
        filter_blank: Optional[Union[str, List[str]]] = None,
        roi: bool = False,
        enable_downsample: bool = True
    ) -> None:
        """Generates square slide thumbnails with black borders of fixed size,
        and saves to project folder.

        Args:
            size (int, optional): Width/height of thumbnail in pixels.
                Defaults to 512.

        Keyword Args:
            dataset (:class:`slideflow.dataset.Dataset`, optional): Dataset
                from which to generate activations. If not supplied, will
                calculate activations for all tfrecords at the tile_px/tile_um
                matching the supplied model, optionally using provided filters
                and filter_blank.
            filters (dict, optional): Filters to use when selecting tfrecords.
                Defaults to None.
            filter_blank (list, optional): Exclude slides blank in these cols.
                Defaults to None.
            roi (bool, optional): Include ROI in the thumbnail images.
                Defaults to False.
            enable_downsample (bool, optional): If True and a thumbnail is not
                embedded in the slide file, downsampling is permitted to
                accelerate thumbnail calculation.
        """
        log.warn(
            "Deprecation warning: Project.generate_thumbnails() will "
            "be moved to Dataset.thumbnails() in slideflow>=1.2"
        )
        thumb_folder = join(self.root, 'thumbs')
        if not exists(thumb_folder):
            os.makedirs(thumb_folder)
        if dataset is None:
            dataset = self.dataset(tile_px=0, tile_um=0)
        dataset = dataset.filter(filters=filters, filter_blank=filter_blank)
        dataset.thumbnails(
            thumb_folder,
            size=size,
            roi=roi,
            enable_downsample=enable_downsample
        )

    def generate_tfrecord_heatmap(
        self,
        tfrecord: str,
        tile_px: int,
        tile_um: Union[int, str],
        tile_dict: Dict[int, float],
        outdir: Optional[str] = None
    ) -> None:
        """Creates a tfrecord-based WSI heatmap using a dictionary of tile
        values for heatmap display, saving to project root directory.

        Args:
            tfrecord (str): Path to tfrecord
            tile_dict (dict): Dictionary mapping tfrecord indices to a
                tile-level value for display in heatmap format
            tile_px (int): Tile width in pixels
            tile_um (int or str): Tile width in microns (int) or magnification
                (str, e.g. "20x").
            outdir (str, optional): Destination path to save heatmap.

        Returns:
            None
        """
        log.warn(
            "Deprecation warning: Project.generate_tfrecord_heatmap() will "
            "be moved to Dataset.tfrecord_heatmap() in slideflow>=1.2"
        )
        dataset = self.dataset(tile_px=tile_px, tile_um=tile_um)
        if outdir is None:
            outdir = self.root
        dataset.tfrecord_heatmap(tfrecord, tile_dict, outdir)

    def dataset(
        self,
        tile_px: Optional[int] = None,
        tile_um: Optional[Union[int, str]] = None,
        *,
        verification: Optional[str] = 'both',
        **kwargs: Any
    ) -> Dataset:
        """Returns :class:`slideflow.Dataset` object using project settings.

        Args:
            tile_px (int): Tile size in pixels
            tile_um (int or str): Tile size in microns (int) or magnification
                (str, e.g. "20x").

        Keyword Args:
            filters (dict, optional): Filters for selecting tfrecords.
                Defaults to None.
            filter_blank (list, optional): Exclude slides blank in these cols.
                Defaults to None.
            min_tiles (int, optional): Min tiles a slide must have.
                Defaults to 0.
            config (str, optional): Path to dataset configuration JSON file.
                Defaults to project default.
            sources (str, list(str), optional): Dataset sources to use from
                configuration. Defaults to project default.
            verification (str, optional): 'tfrecords', 'slides', or 'both'.
                If 'slides', verify all annotations are mapped to slides.
                If 'tfrecords', check that TFRecords exist and update manifest.
                Defaults to 'both'.
        """

        if 'config' not in kwargs:
            kwargs['config'] = self.dataset_config
        if 'sources' not in kwargs:
            kwargs['sources'] = self.sources
        try:
            if self.annotations and exists(self.annotations):
                annotations = self.annotations
            else:
                annotations = None
            dataset = Dataset(
                tile_px=tile_px,
                tile_um=tile_um,
                annotations=annotations,
                **kwargs
            )
        except FileNotFoundError:
            raise errors.DatasetError('No datasets configured.')
        if verification in ('both', 'slides'):
            log.debug("Verifying slide annotations...")
            dataset.verify_annotations_slides()
        if verification in ('both', 'tfrecords'):
            log.debug("Verifying tfrecords...")
            dataset.update_manifest()
        return dataset

    def load_project(self, path: str) -> None:
        """Loads a saved and pre-configured project from the specified path."""

        # Enable logging
        if sf.util.is_project(path):
            self._settings = sf.util.load_json(join(path, 'settings.json'))
        else:
            raise errors.ProjectError('Unable to find settings.json.')

    @auto_dataset
    def predict(
        self,
        model: str,
        *,
        dataset: Dataset,
        filters: Optional[Dict] = None,
        filter_blank: Optional[Union[str, List[str]]] = None,
        min_tiles: int = 0,
        checkpoint: Optional[str] = None,
        eval_k_fold: Optional[int] = None,
        splits: str = "splits.json",
        max_tiles: int = 0,
        batch_size: int = 32,
        format: str = 'csv',
        input_header: Optional[Union[str, List[str]]] = None,
        mixed_precision: bool = True,
        allow_tf32: bool = False,
        load_method: str = 'full',
        custom_objects: Optional[Dict[str, Any]] = None,
        **kwargs: Any
    ) -> "pd.DataFrame":
        """Evaluates a saved model on a given set of tfrecords.

        Args:
            model (str): Path to model to evaluate.

        Keyword Args:
            dataset (:class:`slideflow.dataset.Dataset`, optional): Dataset
                from which to generate predictions. If not supplied, will
                generate predictions for all project tfrecords at the
                tile_px/tile_um matching the model, optionally using provided
                filters and filter_blank.
            filters (dict, optional): Filters to use when selecting tfrecords.
                Defaults to None.
            filter_blank (list, optional): Exclude slides blank in these cols.
                Defaults to None.
            min_tiles (int, optional): Min tiles a slide must have
                to be included. Defaults to 0.
            checkpoint (str, optional): Path to cp.ckpt file, if evaluating a
                saved checkpoint. Defaults to None.
            eval_k_fold (int, optional): K-fold iteration number to evaluate.
                If None, will evaluate all tfrecords irrespective of K-fold.
                Defaults to None.
            splits (str, optional): Filename of JSON file in which to log
                training/validation splits. Looks for filename in project root
                directory. Defaults to "splits.json".
            max_tiles (int, optional): Maximum number of tiles from each slide
                to evaluate. If zero, will include all tiles. Defaults to 0.
            batch_size (int, optional): Batch size to use during prediction.
                Defaults to 32.
            format (str, optional): Format in which to save predictions.
                Either 'csv', 'feather', or 'parquet'. Defaults to 'parquet'.
            input_header (str, optional): Annotation column header to use as
                additional input. Defaults to None.
            mixed_precision (bool, optional): Enable mixed precision.
                Defaults to True.
            allow_tf32 (bool): Allow internal use of Tensorfloat-32 format.
                Defaults to False.
            load_method (str): Either 'full' or 'weights'. Method to use
                when loading a Tensorflow model. If 'full', loads the model with
                ``tf.keras.models.load_model()``. If 'weights', will read the
                ``params.json``configuration file, build the model architecture,
                and then load weights from the given model with
                ``Model.load_weights()``. Loading with 'full' may improve
                compatibility across Slideflow versions. Loading with 'weights'
                may improve compatibility across hardware & environments.
            custom_objects (dict, Optional): Dictionary mapping names
                (strings) to custom classes or functions. Defaults to None.

        Returns:
            Dictionary of predictions dataframes, with the keys 'tile', 'slide',
            and 'patient'.
        """

        # Perform evaluation
        log.info('Predicting model results')
        trainer, eval_dts = self._prepare_trainer(
            model=model,
            dataset=dataset,
            checkpoint=checkpoint,
            eval_k_fold=eval_k_fold,
            splits=splits,
            max_tiles=max_tiles,
            input_header=input_header,
            mixed_precision=mixed_precision,
            allow_tf32=allow_tf32,
            load_method=load_method,
            custom_objects=custom_objects,
        )
        results = trainer.predict(
            dataset=eval_dts,
            batch_size=batch_size,
            format=format,
            **kwargs
        )
        return results

    @auto_dataset
    def predict_wsi(
        self,
        model: str,
        outdir: str,
        *,
        dataset: Dataset,
        filters: Optional[Dict] = None,
        filter_blank: Optional[Union[str, List[str]]] = None,
        min_tiles: int = 0,
        stride_div: int = 1,
        enable_downsample: bool = True,
        roi_method: str = 'auto',
        source: Optional[str] = None,
        img_format: str = 'auto',
        randomize_origin: bool = False,
        **kwargs: Any
    ) -> None:
        """Using a given model, generates a map of tile-level predictions for a
            whole-slide image (WSI), dumping prediction arrays into pkl files
            for later use.

        Args:
            model (str): Path to model from which to generate predictions.
            outdir (str): Directory for saving WSI predictions in .pkl format.

        Keyword Args:
            dataset (:class:`slideflow.dataset.Dataset`, optional): Dataset
                from which to generate activations. If not supplied, will
                calculate activations for all tfrecords at the tile_px/tile_um
                matching the supplied model.
            filters (dict, optional): Filters to use when selecting tfrecords.
                Defaults to None.
            filter_blank (list, optional): Exclude slides blank in these cols.
                Defaults to None.
            min_tiles (int, optional): Min tiles a slide must have
                to be included. Defaults to 0.
            stride_div (int, optional): Stride divisor for extracting tiles.
                A stride of 1 will extract non-overlapping tiles.
                A stride_div of 2 will extract overlapping tiles, with a stride
                equal to 50% of the tile width. Defaults to 1.
            enable_downsample (bool, optional): Enable downsampling for slides.
                This may result in corrupted image tiles if downsampled slide
                layers are corrupted or incomplete. Defaults to True.
            roi_method (str): Either 'inside', 'outside', 'auto', or 'ignore'.
                Determines how ROIs are used to extract tiles.
                If 'inside' or 'outside', will extract tiles in/out of an ROI,
                and raise errors.MissingROIError if an ROI is not available.
                If 'auto', will extract tiles inside an ROI if available,
                and across the whole-slide if no ROI is found.
                If 'ignore', will extract tiles across the whole-slide
                regardless of whether an ROI is available.
                Defaults to 'auto'.
            source (list, optional): Name(s) of dataset sources from which to
                get slides. If None, will use all.
            img_format (str, optional): Image format (png, jpg) to use when
                extracting tiles from slide. Must match the image format
                the model was trained on. If 'auto', will use the format
                logged in the model params.json.
            randomize_origin (bool, optional): Randomize pixel starting
                position during extraction. Defaults to False.
            whitespace_fraction (float, optional): Range 0-1. Defaults to 1.
                Discard tiles with this fraction of whitespace.
                If 1, will not perform whitespace filtering.
            whitespace_threshold (int, optional): Range 0-255. Defaults to 230.
                Threshold above which a pixel (RGB average) is whitespace.
            grayspace_fraction (float, optional): Range 0-1. Defaults to 0.6.
                Discard tiles with this fraction of grayspace.
                If 1, will not perform grayspace filtering.
            grayspace_threshold (float, optional): Range 0-1. Defaults to 0.05.
                Pixels in HSV format with saturation below this are grayspace.
        """

        log.info('Generating WSI prediction / activation maps...')
        if not exists(outdir):
            os.makedirs(outdir)

        if source:
            sources = sf.util.as_list(source)
        else:
            sources = self.sources
        if dataset.tile_px is None or dataset.tile_um is None:
            raise errors.DatasetError(
                "Dataset must have non-zero tile_px and tile_um"
            )
        # Prepare dataset & model
        if img_format == 'auto':
            config = sf.util.get_model_config(model)
            img_format = config['img_format']

        # Log extraction parameters
        sf.slide.log_extraction_params(**kwargs)

        for source in sources:
            log.info(f'Working on dataset source [bold]{source}')
            roi_dir = dataset.sources[source]['roi']

            # Prepare list of slides for extraction
            slide_list = dataset.slide_paths(source=source)
            log.info(f'Generating predictions for {len(slide_list)} slides')

            # Verify slides and estimate total number of tiles
            log.info('Verifying slides...')
            total_tiles = 0
            from rich.progress import track
            for slide_path in track(slide_list, transient=True):
                try:
                    slide = sf.WSI(slide_path,
                                   dataset.tile_px,
                                   dataset.tile_um,
                                   stride_div,
                                   roi_dir=roi_dir,
                                   roi_method=roi_method)
                except errors.SlideError as e:
                    log.error(e)
                else:
                    n_est = slide.estimated_num_tiles
                    log.debug(f"Estimated tiles for slide {slide.name}: {n_est}")
                    total_tiles += n_est
                finally:
                    del slide
            log.info(f'Total estimated tiles: {total_tiles}')

            # Predict for each WSI
            for slide_path in slide_list:
                log.info(f'Working on slide {path_to_name(slide_path)}')
                try:
                    wsi = sf.WSI(slide_path,
                                 dataset.tile_px,
                                 dataset.tile_um,
                                 stride_div,
                                 enable_downsample=enable_downsample,
                                 roi_dir=roi_dir,
                                 roi_method=roi_method,
                                 randomize_origin=randomize_origin)
                except errors.SlideLoadError as e:
                    log.error(e)
                    continue
                except errors.MissingROIError as e:
                    log.error(e)
                    continue
                try:
                    interface = sf.model.Features(model, include_logits=False)
                    wsi_grid = interface(wsi, img_format=img_format)

                    with open(join(outdir, wsi.name+'.pkl'), 'wb') as file:
                        pickle.dump(wsi_grid, file)

                except errors.TileCorruptionError:
                    log.error(f'[green]{path_to_name(slide_path)}[/] is '
                              'corrupt; skipping slide')
                    continue

    def save(self) -> None:
        """Saves current project configuration as "settings.json"."""
        sf.util.write_json(self._settings, join(self.root, 'settings.json'))


    def _get_smac_runner(
        self,
        outcomes: Union[str, List[str]],
        params: sf.ModelParams,
        metric: Union[str, Callable],
        train_kwargs: Any
    ) -> Callable:
        """Builds a SMAC3 optimization runner.

        Args:
            outcomes (str, List[str]): Outcome label annotation header(s).
            params (sf.ModelParams): Model parameters for training.
            metric (str or Callable): Metric to monitor for optimization.
                May be callable function or a str. If a callable function, must
                accept the epoch results dict and return a float value. If
                a str, must be a valid metric, such as  'tile_auc',
                'patient_auc', 'r_squared', etc.
            train_kwargs (dict):  Dict of keyword arguments used for the
                Project.train() function call.

        Raises:
            errors.SMACError: If training does not return the designated metric.

        Returns:
            Callable: tae_runner for SMAC optimization.
        """

        def smac_runner(config):
            """SMAC tae_runner function."""

            # Load hyperparameters from SMAC configuration and train model.
            params.load_dict(dict(config))
            results = self.train(
                outcomes=outcomes,
                params=params,
                **train_kwargs
            )

            # Interpret results.
            model_name = list(results.keys())[0]
            last_epoch = sorted(list(results[model_name]['epochs'].keys()))[-1]
            if len(results[model_name]['epochs']) > 1:
                log.warning(f"Ambiguous epoch for SMAC. Using '{last_epoch}'.")
            epoch_results = results[model_name]['epochs'][last_epoch]

            # Determine metric for optimization.
            if callable(metric):
                return metric(epoch_results)
            elif metric not in epoch_results:
                raise errors.SMACError(f"Metric '{metric}' not returned from "
                                       "training, unable to optimize.")
            else:
                if outcomes not in epoch_results[metric]:
                    raise errors.SMACError(
                        f"Unable to interpret metric {metric} (epoch results: "
                        f"{epoch_results})")
                return 1 - mean(epoch_results[metric][outcomes])

        return smac_runner

    def smac_search(
        self,
        outcomes: Union[str, List[str]],
        params: ModelParams,
        smac_configspace: "ConfigurationSpace",
        smac_limit: int = 10,
        smac_metric: str = 'tile_auc',
        **train_kwargs: Any
    ) -> None:
        """Train a model using SMAC3 bayesian hyperparameter optimization.

        The hyperparameter optimization is performed with
        `SMAC3 <https://automl.github.io/SMAC3/master/>`_. Start by setting the
        `configuration space <https://automl.github.io/ConfigSpace/master/>`_:

        .. code-block:: python

            from ConfigSpace.hyperparameters import UniformFloatHyperparameter
            from ConfigSpace import ConfigurationSpace

            cs = ConfigurationSpace()
            cs.add_hyperparameter(UniformIntegerHyperparameter("l1", 0, .2))
            cs.add_hyperparameter(UniformFloatHyperparameter("dropout", 0, 0.5))

        Then, use this ``smac_search()`` function as you would use
        ``Project.train()``, passing the configuration space to the
        ``smac_configspace`` argument:

            >>> P.train(..., smac_configspace=cs)

        Args:
            outcomes (str, List[str]): Outcome label annotation header(s).
            params (ModelParams): Model parameters for training.
            smac_configspace (ConfigurationSpace): ConfigurationSpace to
                determine the SMAC optimization.
            smac_limit (int): Max number of function evaluations to perform
                during optimization. Defaults to 10.
            smac_metric (str, optional): Metric to monitor for optimization.
                May either be a callable function or a str. If a callable
                function, must accept the epoch results dict and return a
                float value. If a str, must be a valid metric, such as
                'tile_auc', 'patient_auc', 'r_squared', etc.
                Defaults to 'tile_auc'.

        Returns:
            Configuration: Optimal hyperparameter configuration returned
            by SMAC4BB.optimize()
        """

        from smac.facade.smac_bb_facade import SMAC4BB
        from smac.scenario.scenario import Scenario

        # Create SMAC scenario.
        scenario = Scenario({
            'run_obj': 'quality', # Optimize quality (alternatively: runtime)
            'runcount-limit': smac_limit,  # Max number of function evaluations
            'cs': smac_configspace
        })
        smac = SMAC4BB(
            scenario=scenario,
            tae_runner=self._get_smac_runner(
                outcomes=outcomes,
                params=params,
                metric=smac_metric,
                train_kwargs=train_kwargs,
            )
        )

        # Optimize.
        best_config = smac.optimize()
        log.info("Results of SMAC optimization:")
        print(best_config)
        return best_config

    def train(
        self,
        outcomes: Union[str, List[str]],
        params: Union[str,
                      ModelParams,
                      List[ModelParams],
                      Dict[str, ModelParams]],
        *,
        exp_label: Optional[str] = None,
        filters: Optional[Dict] = None,
        filter_blank: Optional[Union[str, List[str]]] = None,
        input_header: Optional[Union[str, List[str]]] = None,
        min_tiles: int = 0,
        max_tiles: int = 0,
        splits: str = "splits.json",
        mixed_precision: bool = True,
        allow_tf32: bool = False,
        load_method: str = 'full',
        balance_headers: Optional[Union[str, List[str]]] = None,
        process_isolate: bool = False,
        **training_kwargs: Any
    ) -> Dict:
        """Train model(s) using a given set of parameters, outcomes, and inputs.

        Args:
            outcomes (str or list(str)): Outcome label annotation header(s).
            params (:class:`slideflow.model.ModelParams`, list, dict, or str):
                Model parameters for training. May provide one `ModelParams`,
                a list, or dict mapping model names to params. If multiple
                params are provided, will train models for each. If JSON file
                is provided, will interpret as a hyperparameter sweep. See
                examples below for use.

        Keyword Args:
            exp_label (str, optional): Experiment label to add model names.
            filters (dict, optional): Filters to use when selecting tfrecords.
                Defaults to None.
            filter_blank (list, optional): Exclude slides blank in these cols.
                Defaults to None.
            input_header (list, optional): List of annotation column headers to
                use as additional slide-level model input. Defaults to None.
            min_tiles (int): Minimum number of tiles a slide must have to
                include in training. Defaults to 0.
            max_tiles (int): Only use up to this many tiles from each slide for
                training. Defaults to 0 (include all tiles).
            splits (str, optional): Filename of JSON file in which to log
                train/val splits. Looks for filename in project root directory.
                Defaults to "splits.json".
            mixed_precision (bool, optional): Enable mixed precision.
                Defaults to True.
            allow_tf32 (bool): Allow internal use of Tensorfloat-32 format.
                Defaults to False.
            load_method (str): Either 'full' or 'weights'. Method to use
                when loading a Tensorflow model. If 'full', loads the model with
                ``tf.keras.models.load_model()``. If 'weights', will read the
                ``params.json``configuration file, build the model architecture,
                and then load weights from the given model with
                ``Model.load_weights()``. Loading with 'full' may improve
                compatibility across Slideflow versions. Loading with 'weights'
                may improve compatibility across hardware & environments.
            balance_headers (str or list(str)): Annotation header(s) specifying
                labels on which to perform mini-batch balancing. If performing
                category-level balancing and this is set to None, will default
                to balancing on outcomes. Defaults to None.
            val_strategy (str): Validation dataset selection strategy. Options
                include bootstrap, k-fold, k-fold-manual,
                k-fold-preserved-site, fixed, and none. Defaults to 'k-fold'.
            val_k_fold (int): Total number of K if using K-fold validation.
                Defaults to 3.
            val_k (int): Iteration of K-fold to train, starting at 1. Defaults
                to None (training all k-folds).
            val_k_fold_header (str): Annotations file header column for
                manually specifying k-fold or for preserved-site cross
                validation. Only used if validation strategy is 'k-fold-manual'
                or 'k-fold-preserved-site'. Defaults to None for k-fold-manual
                and 'site' for k-fold-preserved-site.
            val_fraction (float): Fraction of dataset to use for validation
                testing, if strategy is 'fixed'.
            val_source (str): Dataset source to use for validation. Defaults to
                None (same as training).
            val_annotations (str): Path to annotations file for validation
                dataset. Defaults to None (same as training).
            val_filters (dict): Filters to use for validation dataset.
                Defaults to None (same as training).
            checkpoint (str, optional): Path to cp.ckpt from which to load
                weights. Defaults to None.
            pretrain (str, optional): Either 'imagenet' or path to Tensorflow
                model from which to load weights. Defaults to 'imagenet'.
            multi_gpu (bool): Train using multiple GPUs when available.
                Defaults to False.
            resume_training (str, optional): Path to Tensorflow model to
                continue training. Defaults to None.
            starting_epoch (int): Start training at the specified epoch.
                Defaults to 0.
            steps_per_epoch_override (int): If provided, will manually set the
                number of steps in an epoch. Default epoch length is the number
                of total tiles.
            save_predictions (bool or str, optional): Save tile, slide, and
                patient-level predictions at each evaluation. May be 'csv',
                'feather', or 'parquet'. If False, will not save predictions.
                Defaults to 'parquet'.
            save_model (bool, optional): Save models when evaluating at
                specified epochs. Defaults to True.
            validate_on_batch (int): Perform validation every N batches.
                Defaults to 0 (only at epoch end).
            validation_batch_size (int): Validation dataset batch size.
                Defaults to 32.
            use_tensorboard (bool): Add tensorboard callback for realtime
                training monitoring. Defaults to False.
            validation_steps (int): Number of steps of validation to perform
                each time doing a mid-epoch validation check. Defaults to 200.

        Returns:
            Dict with model names mapped to train_acc, val_loss, and val_acc

        Examples
            Method 1 (hyperparameter sweep from a configuration file):

                >>> P.train('outcome', params='sweep.json', ...)

            Method 2 (manually specified hyperparameters):

                >>> hp = sf.ModelParams(...)
                >>> P.train('outcome', params=hp, ...)

            Method 3 (list of hyperparameters):

                >>> hp = [sf.ModelParams(...), sf.ModelParams(...)]
                >>> P.train('outcome', params=hp, ...)

            Method 4 (dict of hyperparameters):

                >>> hp = {'HP0': sf.ModelParams(...), ...}
                >>> P.train('outcome', params=hp, ...)

        """

        # Prepare outcomes
        if not isinstance(outcomes, list):
            outcomes = [outcomes]
        if len(outcomes) > 1:
            log.info(f'Training with {len(outcomes)} outcomes')
            log.info(f'Outcomes: {", ".join(outcomes)}')

        # Prepare hyperparameters
        if isinstance(params, str):
            if exists(params):
                hp_dict = sf.model.read_hp_sweep(params)
            elif exists(join(self.root, params)):
                hp_dict = sf.model.read_hp_sweep(join(self.root, params))
            else:
                raise errors.ModelParamsError(f"Unable to find file {params}")
        elif isinstance(params, ModelParams):
            hp_dict = {'HP0': params}
        elif isinstance(params, list):
            if not all([isinstance(hp, ModelParams) for hp in params]):
                raise errors.ModelParamsError(
                    'If params is a list, items must be sf.model.ModelParams'
                )
            hp_dict = {f'HP{i}': hp for i, hp in enumerate(params)}
        elif isinstance(params, dict):
            if not all([isinstance(hp, str) for hp in params.keys()]):
                raise errors.ModelParamsError(
                    'If params is a dict, keys must be of type str'
                )
            all_hp = params.values()
            if not all([isinstance(hp, ModelParams) for hp in all_hp]):
                raise errors.ModelParamsError(
                    'If params is a dict, values must be sf.ModelParams'
                )
            hp_dict = params
        else:
            raise ValueError(f"Unable to interprest params value {params}")

        # Get default validation settings from kwargs
        val_kwargs = {
            k[4:]: v for k, v in training_kwargs.items() if k[:4] == 'val_'
        }
        training_kwargs = {
            k: v for k, v in training_kwargs.items() if k[:4] != 'val_'
        }
        val_settings = get_validation_settings(**val_kwargs)
        _invalid = (
            'k-fold-manual',
            'k-fold-preserved-site',
            'k-fold',
            'bootstrap'
        )
        if (val_settings.strategy in _invalid) and val_settings.source:
            _m = f'{val_settings.strategy} invalid with val_source != None'
            raise ValueError(_m)

        # Next, prepare the multiprocessing manager (needed to free VRAM after
        # training and keep track of results)
        manager = multiprocessing.Manager()
        results_dict = manager.dict()
        ctx = multiprocessing.get_context('spawn')

        # === Train with a set of hyperparameters =============================
        for hp_name, hp in hp_dict.items():
            if exp_label:
                hp_name = f'{exp_label}-{hp_name}'
            self._train_hp(
                hp_name=hp_name,
                hp=hp,
                outcomes=outcomes,
                val_settings=val_settings,
                ctx=ctx,
                filters=filters,
                filter_blank=filter_blank,
                input_header=input_header,
                min_tiles=min_tiles,
                max_tiles=max_tiles,
                mixed_precision=mixed_precision,
                allow_tf32=allow_tf32,
                splits=splits,
                balance_headers=balance_headers,
                training_kwargs=training_kwargs,
                results_dict=results_dict,
                load_method=load_method,
                process_isolate=process_isolate
            )
        # Print summary of all models
        log.info('Training complete; validation accuracies:')
        for model in results_dict:
            if 'epochs' not in results_dict[model]:
                continue
            ep_res = results_dict[model]['epochs']
            epochs = [e for e in ep_res if 'epoch' in e]
            try:
                last = max([int(e.split('epoch')[-1]) for e in epochs])
                final_train_metrics = ep_res[f'epoch{last}']['train_metrics']
            except ValueError:
                pass
            else:
                log.info(f'[green]{model}[/] training metrics:')
                for m in final_train_metrics:
                    log.info(f'{m}: {final_train_metrics[m]}')
                if 'val_metrics' in ep_res[f'epoch{last}']:
                    final_val_metrics = ep_res[f'epoch{last}']['val_metrics']
                    log.info(f'[green]{model}[/] validation metrics:')
                    for m in final_val_metrics:
                        log.info(f'{m}: {final_val_metrics[m]}')
        return dict(results_dict)

    def train_clam(
        self,
        exp_name: str,
        pt_files: str,
        outcomes: Union[str, List[str]],
        dataset: Dataset,
        train_slides: Union[str, List[str]] = 'auto',
        val_slides: Union[str, List[str]] = 'auto',
        splits: str = 'splits.json',
        clam_args: Optional[SimpleNamespace] = None,
        attention_heatmaps: bool = True
    ) -> None:
        """Train a CLAM model from layer activations exported with
        :meth:`slideflow.project.generate_features_for_clam`.

        Args:
            exp_name (str): Name of experiment. Makes clam/{exp_name} folder.
            pt_files (str): Path to pt_files containing tile-level features.
            outcomes (str): Annotation column which specifies the outcome.
            dataset (:class:`slideflow.dataset.Dataset`): Dataset object from
                which to generate activations.
            train_slides (str, optional): List of slide names for training.
                If 'auto' (default), will auto-generate training/val split.
            validation_slides (str, optional): List of slides for validation.
                If 'auto' (default), will auto-generate training/val split.
            splits (str, optional): Filename of JSON file in which to log
                training/val splits. Looks for filename in project root
                directory. Defaults to "splits.json".
            clam_args (optional): Namespace with clam arguments, as provided
                by :func:`slideflow.clam.get_args`.
            attention_heatmaps (bool, optional): Save attention heatmaps of
                validation dataset.

        Returns:
            None

        Examples
            Train with basic settings:

                >>> dataset = P.dataset(tile_px=299, tile_um=302)
                >>> P.generate_features_for_clam('/model', outdir='/pt_files')
                >>> P.train_clam('NAME', '/pt_files', 'category1', dataset)

            Specify a specific layer from which to generate activations:

                >>> P.generate_features_for_clam(..., layers=['postconv'])

            Manually configure CLAM, with 5-fold validation and SVM bag loss:

                >>> import slideflow.clam as clam
                >>> clam_args = clam.get_args(k=5, bag_loss='svm')
                >>> P.generate_features_for_clam(...)
                >>> P.train_clam(..., clam_args=clam_args)
        """

        import slideflow.clam as clam
        from slideflow.clam.create_attention import export_attention
        from slideflow.clam.datasets.dataset_generic import Generic_MIL_Dataset

        # Set up CLAM experiment data directory
        clam_dir = join(self.root, 'clam', exp_name)
        results_dir = join(clam_dir, 'results')
        splits_file = join(self.root, splits)
        if not exists(results_dir):
            os.makedirs(results_dir)

        # Get base CLAM args/settings if not provided.
        if not clam_args:
            clam_args = clam.get_args()
        assert isinstance(clam_args, SimpleNamespace)

        # Detect number of features automatically from saved pt_files
        pt_file_paths = [
            join(pt_files, p) for p in os.listdir(pt_files)
            if sf.util.path_to_ext(join(pt_files, p)) == 'pt'
        ]
        num_features = clam.detect_num_features(pt_file_paths[0])

        # Note: CLAM only supports categorical outcomes
        labels, unique_labels = dataset.labels(outcomes, use_float=False)

        if train_slides == val_slides == 'auto':
            k_train_slides = {}  # type: Dict
            k_val_slides = {}  # type: Dict
            for k in range(clam_args.k):
                train_dts, val_dts = dataset.train_val_split(
                    'categorical',
                    labels,
                    val_strategy='k-fold',
                    splits=splits_file,
                    val_k_fold=clam_args.k,
                    k_fold_iter=k+1
                )
                k_train_slides[k] = [
                    path_to_name(t) for t in train_dts.tfrecords()
                ]
                k_val_slides[k] = [
                    path_to_name(t) for t in val_dts.tfrecords()
                ]
        else:
            k_train_slides = {0: train_slides}
            k_val_slides = {0: val_slides}

        # Remove slides without associated .pt files
        num_skipped = 0
        for k in k_train_slides:
            n_supplied = len(k_train_slides[k]) + len(k_val_slides[k])
            k_train_slides[k] = [
                s for s in k_train_slides[k] if exists(join(pt_files, s+'.pt'))
            ]
            k_val_slides[k] = [
                s for s in k_val_slides[k] if exists(join(pt_files, s+'.pt'))
            ]
            n_train = len(k_train_slides[k])
            n_val = len(k_val_slides[k])
            num_skipped += n_supplied - (n_train + n_val)
        if num_skipped:
            log.warn(f'Skipping {num_skipped} slides missing .pt files.')

        # Set up training/validation splits (mirror base model)
        split_dir = join(clam_dir, 'splits')
        if not exists(split_dir):
            os.makedirs(split_dir)
        header = ['', 'train', 'val', 'test']
        for k in range(clam_args.k):
            with open(join(split_dir, f'splits_{k}.csv'), 'w') as f:
                writer = csv.writer(f)
                writer.writerow(header)
                # Currently, the below sets the val & test sets to be the same
                for i in range(max(len(k_train_slides[k]),
                                   len(k_val_slides[k]))):
                    row = [i]  # type: List
                    if i < len(k_train_slides[k]):
                        row += [k_train_slides[k][i]]
                    else:
                        row += ['']
                    if i < len(k_val_slides[k]):
                        row += [k_val_slides[k][i], k_val_slides[k][i]]
                    else:
                        row += ['', '']
                    writer.writerow(row)

        # Assign CLAM settings based on this project
        clam_args.model_size = [num_features, 256, 128]
        clam_args.results_dir = results_dir
        clam_args.n_classes = len(unique_labels)
        clam_args.split_dir = split_dir
        clam_args.data_root_dir = pt_files

        # Save clam settings
        sf.util.write_json(vars(clam_args), join(clam_dir, 'experiment.json'))

        # Create CLAM dataset
        clam_dataset = Generic_MIL_Dataset(
            csv_path=self.annotations,
            data_dir=pt_files,
            shuffle=False,
            seed=clam_args.seed,
            print_info=True,
            label_col=outcomes,
            label_dict=dict(zip(unique_labels, range(len(unique_labels)))),
            patient_strat=False,
            ignore=[]
        )
        # Run CLAM
        clam.main(clam_args, clam_dataset)

        # Get attention from trained model on validation set(s)
        for k in k_val_slides:
            tfr = dataset.tfrecords()
            attention_tfrecords = [
                t for t in tfr if path_to_name(t) in k_val_slides[k]
            ]
            attention_dir = join(clam_dir, 'attention', str(k))
            if not exists(attention_dir):
                os.makedirs(attention_dir)
            rev_labels = dict(zip(range(len(unique_labels)), unique_labels))
            export_attention(
                vars(clam_args),
                ckpt_path=join(results_dir, f's_{k}_checkpoint.pt'),
                outdir=attention_dir,
                pt_files=pt_files,
                slides=k_val_slides[k],
                reverse_labels=rev_labels,
                labels=labels
            )
            if attention_heatmaps:
                heatmaps_dir = join(clam_dir, 'attention_heatmaps', str(k))
                if not exists(heatmaps_dir):
                    os.makedirs(heatmaps_dir)

                for att_tfr in attention_tfrecords:
                    attention_dict = {}
                    slide = path_to_name(att_tfr)
                    try:
                        with open(join(attention_dir, slide+'.csv'), 'r') as f:
                            reader = csv.reader(f)
                            for row in reader:
                                attention_dict.update({
                                    int(row[0]): float(row[1])
                                })
                    except FileNotFoundError:
                        print(f'Attention scores for slide {slide} not found')
                        continue
                    dataset.tfrecord_heatmap(
                        att_tfr,
                        tile_dict=attention_dict,
                        outdir=heatmaps_dir
                    )

# -----------------------------------------------------------------------------

def create(
    root: str,
    cfg: Union[str, Dict],
    *,
    download: bool = False,
    md5: bool = False,
    **kwargs
) -> "Project":
    """Create a project at the existing folder from a given configuration.

    Supports both manual project creation via keyword arguments, and setting
    up a project through a specified configuration. The configuration may be
    a dictionary or a path to a JSON file containing a dictionary. It must
    have the key 'annotations', which includes a path to an annotations file,
    and may optionally have the following arguments:

        - 'name'        Name for the project and dataset.
        - 'rois'        Path to .tar.gz file containing compressed ROIs.
        - 'slides'      Path in which slides will be stored.
        - 'tiles'       Path in which extracted tiles will be stored.
        - 'tfrecords'   Path in which TFRecords will be stored.

    Annotations files are copied into the created project folder.

    Args:
        root (str): Path at which the Project will be set up.
        cfg (dict, str): Path to configuration file (JSON), or a dictionary,
            containing the key "annotations", and optionally with the keys
            "name", "rois", "slides", "tiles", or "tfrecords".

    Keyword Args:
        download (bool): Download any missing slides from the Genomic Data
            Commons (GDC) automatically, using slide names stored in the
            annotations file.
        md5 (bool): Perform MD5 hash verification for all slides using
            the GDC (TCGA) MD5 manifest, which will be automatically downloaded.
        name (str): Set the project name. This has higher priority than the
            supplied configuration, which will be ignored.
        slides (str): Set the destination folder for slides. This has higher
            priority than the supplied configuration, which will be ignored.
        tiles (str): Set the destination folder for tiles. This has higher
            priority than the supplied configuration, which will be ignored.
        tfrecords (str): Set the destination for TFRecords. This has higher
            priority than the supplied configuration, which will be ignored.
        roi_dest (str): Set the destination folder for ROIs.

    Returns:
        slideflow.Project
    """

    # Initial verification
    if sf.util.is_project(root):
        raise OSError(f"A project already exists at {root}")
    if isinstance(cfg, dict):
        cfg = sf.util.EasyDict(cfg)
    if isinstance(cfg, str):
        cfg_path = cfg
        cfg = sf.util.EasyDict(sf.util.load_json(cfg))

        # Resolve relative paths in configuration file
        if 'annotations' in cfg and exists(join(dirname(cfg_path),
                                                cfg.annotations)):
            cfg.annotations = join(dirname(cfg_path), cfg.annotations)
        if 'rois' in cfg and exists(join(dirname(cfg_path), cfg.rois)):
            cfg.rois = join(dirname(cfg_path), cfg.rois)
    if 'annotations' not in cfg:
        raise ValueError("'annotations' must be provided in configuration.")
    if 'name' not in cfg:
        cfg.name = "MyProject"
    if 'slides' not in cfg:
        cfg.slides = join(root, 'slides')
    if 'tiles' not in cfg:
        cfg.tiles = join(root, 'tiles')
    if 'tfrecords' not in cfg:
        cfg.tfrecords = join(root, 'tfrecords')
    cfg.roi_dest = join(cfg.slides, 'rois')

    # Overwrite any project configuration with user-specified keyword arguments
    cfg.update(kwargs)

    # Set up project at the given directory.
    log.info(f"Setting up project at {root}")
    P = sf.Project(root, annotations=join(root, basename(cfg.annotations)))
    shutil.copy(cfg.annotations, root)
    P.add_source(
        cfg.name,
        slides=cfg.slides,
        roi=cfg.roi_dest,
        tiles=cfg.tiles,
        tfrecords=cfg.tfrecords)

    # Set up ROIs, if provided.
    if 'rois' in cfg and not exists(cfg.roi_dest):
        os.makedirs(cfg.roi_dest)
    if 'rois' in cfg and exists(cfg.rois) and os.path.isdir(cfg.rois):
        # Search the folder for CSV files and copy to the project ROI directory.
        to_copy = [r for r in os.listdir(cfg.rois) if path_to_ext(r) == 'csv']
        log.info("Copying {} ROIs from {} to {}.".format(
            len(to_copy),
            cfg.rois,
            cfg.roi_dest
        ))
        for roi in to_copy:
            shutil.copy(join(cfg.rois, roi), cfg.roi_dest)
    elif 'rois' in cfg and exists(cfg.rois) and os.path.isfile(cfg.rois):
        # Assume ROIs is a tarfile - extract at destination.
        log.info(f"Extrating ROIs from tarfile at {cfg.rois}.")
        roi_file = tarfile.open(cfg.rois)
        roi_file.extractall(cfg.roi_dest)

    # Download slides from GDC (TCGA), if specified.
    if download:
        df = sf.util.get_gdc_manifest()
        slide_manifest = dict(zip(df.filename.values, df.id.values))
        if not exists(cfg.slides):
            os.makedirs(cfg.slides)
        to_download = [s for s in P.dataset().slides()
                       if not exists(join(cfg.slides, f'{s}.svs'))]
        for i, slide in enumerate(to_download):
            sf.util.download_from_tcga(
                slide_manifest[slide+".svs"],
                dest=cfg.slides,
                message=f"Downloading {i+1} of {len(to_download)}...")

    # Perform MD5 hash verification of slides using the GDC manifest.
    if md5:
        df = sf.util.get_gdc_manifest()
        md5_manifest = dict(zip(df.filename.values, df.md5.values))

        slides_with_md5 = [s for s in os.listdir(cfg.slides)
                           if s in md5_manifest]
        failed_md5 = []
        for slide in tqdm(slides_with_md5):
            if sf.util.md5(join(cfg.slides, slide)) != md5_manifest[slide]:
                log.info(f"Slide {slide} failed MD5 verification")
                failed_md5 += [slide]
        if not failed_md5:
            log.info(f"All {len(slides_with_md5)} slides passed MD5 verification.")
        else:
            log.warn(f"Warning: {len(failed_md5)} slides failed MD5 verification:")

    return P
