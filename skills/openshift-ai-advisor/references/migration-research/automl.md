# AutoML

RHOAI **Technology Preview** automated search over algorithms and hyperparameters for **structured prediction** from **CSV** (binary/multiclass classification, regression, time-series forecasting). Runs AutoGluon-backed Kubeflow pipelines, produces a leaderboard + notebooks, and can register/serve the winner. Requires Distributed Workloads (Kueue, Ray and/or Training Operator) + Workbenches. Peers are DIY tabular AutoML libraries, Optuna/Ray Tune/`GridSearchCV` HPO loops, and low-code compare-models stacks that teams run instead of (or before) catalog AutoML.

## Peers

- AutoGluon (DIY / local) — `TabularPredictor` / `TimeSeriesPredictor` `.fit` + `.leaderboard` in notebooks or custom jobs; **engine collision** with RHOAI AutoML (same AutoGluon stack, unmanaged path)
- FLAML — Microsoft AutoML (`from flaml import AutoML`; `automl.fit(X, y, task=…)`)
- TPOT — genetic pipeline search (`TPOTClassifier` / `TPOTRegressor`; `tpot.export('pipeline.py')`)
- auto-sklearn — Bayesian CASH (`AutoSklearnClassifier` / `AutoSklearnRegressor`)
- H2O AutoML — `H2OAutoML()`, `am.leaderboard`
- PyCaret — low-code `setup` + `compare_models` / `tune_model`
- MLJAR supervised — `mljar-supervised` / `AutoML()` leaderboard folder artifacts
- Optuna sweeps — `optuna.create_study` / `study.optimize` / `trial.suggest_*` (and `OptunaSearchCV`) over sklearn/boosting tabular pipelines
- Ray Tune sweeps — `tune.Tuner` / `tune.run` + `param_space` / ASHA over sklearn/XGBoost/LightGBM trainables (tabular HPO; not multi-node Train infra)
- sklearn GridSearchCV / RandomizedSearchCV DIY — `GridSearchCV`, `RandomizedSearchCV`, `HalvingGridSearchCV` / `HalvingRandomSearchCV`, `param_grid` / `best_estimator_`
- Manual nested HP loops — `ParameterGrid`, nested `for` over depths/estimators + `cross_val_score`, hand-built leaderboard CSV
- Hyperopt / Keras Tuner / W&B Sweeps — `fmin`/`tpe.suggest`, `keras_tuner`/`kt.Hyperband`, `wandb.sweep` when the objective is tabular model/HP selection (not DL architecture search alone)

**Not peers (adjacent catalog jobs):** **AutoRAG** (RAG chunk/embed/retriever sweeps); **Model Customization** / **Distributed Workloads** (LLM fine-tune or multi-node Train without tabular search); **Data Science Pipelines** alone (generic KFP without AutoGluon AutoML runs); **LMEval** / **RAGAS** (generative/RAG eval); fixed single estimator → **Workbenches** + **MLServer**/**OVMS**.

## Detection aliases

- AutoGluon DIY: `autogluon`, `from autogluon.tabular import TabularPredictor`, `TabularPredictor(label=`, `.leaderboard`, `from autogluon.timeseries import TimeSeriesPredictor`, `TimeSeriesDataFrame`, `prediction_length`
- FLAML: `flaml`, `from flaml import AutoML`, `automl.fit(`, `task="classification"` / `task="regression"`
- TPOT: `tpot`, `TPOTClassifier`, `TPOTRegressor`, `tpot.export(`
- auto-sklearn: `auto-sklearn`, `autosklearn`, `AutoSklearnClassifier`, `AutoSklearnRegressor`
- H2O: `h2o`, `H2OAutoML`, `am.leaderboard`, `h2o.automl`
- PyCaret: `pycaret`, `from pycaret`, `compare_models`, `tune_model`, `setup(`
- MLJAR: `mljar-supervised`, `mljar`, `from supervised import AutoML`
- Optuna: `optuna`, `optuna.create_study`, `study.optimize`, `trial.suggest_int` / `suggest_float` / `suggest_categorical`, `OptunaSearchCV`, `TPESampler`, `study.best_params`
- Ray Tune: `from ray import tune`, `tune.Tuner`, `tune.run`, `param_space`, `tune.uniform` / `tune.choice` / `ASHAScheduler`, `ray.tune.report`
- sklearn search: `GridSearchCV`, `RandomizedSearchCV`, `HalvingGridSearchCV`, `HalvingRandomSearchCV`, `param_grid=`, `param_distributions=`, `best_params_`, `best_estimator_`, `cv_results_`
- Manual / other HPO: `ParameterGrid`, `cross_val_score` in nested loops, `hyperopt` / `fmin` / `tpe.suggest`, `keras_tuner` / `kt.Hyperband`, `wandb.sweep`, `leaderboard.csv` from bake-offs
- Intent: “hyperparameter tuning”, “model selection”, “Bayesian HPO”, multi-algo RF/XGBoost/LightGBM/CatBoost compare tables on CSV
- RHOAI already-on path: `autogluon-tabular-training-pipeline`, `autogluon-timeseries-training-pipeline`, `pipelines/training/automl/`, dashboard AutoML optimization run, CSV/S3 upload + Binary/Multiclass/Regression/Time Series task type

## Row (for table)

| AutoGluon (DIY TabularPredictor/TimeSeriesPredictor); FLAML; TPOT; auto-sklearn; H2O AutoML; PyCaret; MLJAR supervised; Optuna / OptunaSearchCV tabular sweeps; Ray Tune tabular HPO; GridSearchCV / RandomizedSearchCV / Halving*SearchCV DIY; manual ParameterGrid / nested HP loops; Hyperopt / Keras Tuner / W&B Sweeps (tabular model selection) | AutoML | autogluon / TabularPredictor / TimeSeriesPredictor / .leaderboard; flaml / from flaml import AutoML; TPOTClassifier / TPOTRegressor; AutoSklearnClassifier; H2OAutoML / am.leaderboard; pycaret / compare_models; mljar-supervised; optuna.create_study / trial.suggest_* / OptunaSearchCV; ray.tune / tune.Tuner / ASHAScheduler; GridSearchCV / RandomizedSearchCV / param_grid / best_estimator_; ParameterGrid / nested for + cross_val_score; hyperopt fmin; keras_tuner; wandb.sweep; autogluon-tabular-training-pipeline / autogluon-timeseries-training-pipeline / pipelines/training/automl/ |
