# Workbenches

Browser-based **interactive development environments** (JupyterLab, VS Code/code-server, RStudio) with DS libraries, GPU access, PVC home storage, and cluster connections—provisioned via dashboard or `Notebook` CRDs. Peers are multi-user notebook platforms, managed cloud IDE studios, and DIY Jupyter/VS Code/RStudio pods that teams use instead of (or before) adopting RHOAI Workbenches.

## Peers

- JupyterHub / Zero-to-JupyterHub (Z2JH) — multi-user Hub + `KubeSpawner`/`DockerSpawner` spawning per-user notebook pods (Helm `jupyterhub/jupyterhub`)
- Kubeflow Notebooks — Kubeflow `Notebook` CR / central dashboard notebook servers (upstream of ODH/RHOAI workbench CRD)
- DIY Jupyter Deployments — hand-rolled JupyterLab/Notebook `Deployment`+`Service`+`Route`/`Ingress`+PVC (no Hub, no `Notebook` CR)
- Docker / Compose Jupyter stacks — `jupyter/docker-stacks`, `quay.io/jupyter/*-notebook`, GPU-Jupyter compose on `:8888`
- code-server / VS Code ML pods — browser VS Code (`codercom/code-server`) or VS Code Server Deployments with GPU + workspace PVC for ML
- RStudio Server DIY — standalone `rstudio-server` containers/Deployments for R ML workflows outside RHOAI images
- Amazon SageMaker Studio — managed Studio/JupyterLab spaces, domains, and notebook instances on AWS
- Google Vertex AI Workbench / Colab Enterprise — managed Jupyter notebooks and Workbench instances on GCP
- Azure Machine Learning compute instances / notebooks — managed AML notebook VMs and Studio notebooks
- Databricks notebooks — workspace notebook UX on Databricks clusters (interactive DS, not RHOAI CRDs)
- Domino Data Lab / Anaconda Enterprise — enterprise DS workspaces with hosted notebooks and environments
- Binder / repo2docker — ephemeral Jupyter from git repos (`mybinder.org`, `jupyter-repo2docker`)
- Shared bastion / SSH GPU boxes — team SSH into a shared machine with conda/Jupyter (no cluster IDE lifecycle)

## Detection aliases

- JupyterHub / Z2JH: `jupyterhub`, `jupyterhub_config.py`, `c.KubeSpawner.`, `KubeSpawner`, `zero-to-jupyterhub`, Helm chart `jupyterhub/jupyterhub`, `singleuser.image`, `hub.config.KubeSpawner`, `jupyterhub-deploy-docker`, `DockerSpawner`
- Kubeflow Notebooks: `kind: Notebook` + `kubeflow.org/v1` (non-ODH cluster), Kubeflow central dashboard notebooks, `notebook-controller`
- DIY Jupyter Deployments: custom notebook `Deployment`+`Route`/`Ingress`+PVC; image `jupyter/*-notebook` / `start-notebook.sh|py`; no `notebooks.opendatahub.io/*`
- Docker / Compose Jupyter: `docker-compose` + Jupyter, `JUPYTER_ENABLE_LAB`, `start-notebook.py`, `NOTEBOOK_ARGS`, `ServerApp.`, port `:8888`, volume `/home/jovyan`, `cschranz/gpu-jupyter`
- code-server / VS Code ML pods: `code-server`, `codercom/code-server`, `code-server --bind-addr`, VS Code Server Deployment+PVC+GPU for ML
- RStudio Server DIY: `rstudio-server`, `rocker/rstudio`, RStudio Deployment+Service (not RHOAI `rstudio-rhel9` ImageStream)
- SageMaker Studio: `sagemaker.CreateDomain`, `SageMaker Studio`, `aws sagemaker create-notebook-instance`, `SagemakerNotebookInstance`, Studio JupyterLab spaces
- Vertex AI Workbench / Colab: `aiplatform.Notebook`, `Vertex AI Workbench`, `gcloud notebooks`, `colab.research.google.com`, Colab Enterprise
- Azure ML notebooks: `azure.ai.ml`, AML compute instance, `az ml compute`, Azure ML Studio notebooks
- Databricks notebooks: `databricks` workspace notebooks, `.dbc` / Databricks Repos notebook paths
- Domino / Anaconda Enterprise: `dominodatalab`, Domino workspaces, Anaconda Enterprise / Data Science Platform notebooks
- Binder / repo2docker: `mybinder.org`, `repo2docker`, `jupyter-repo2docker`, `binderhub`
- Shared SSH GPU boxes: SSH + `jupyter lab` / `jupyter notebook` on a shared host; no Hub/CRD/PVC IDE pattern
- Cross-cutting IDE markers: `*.ipynb`, `.jupyter/`, `jupyter_server_config.py`, `jupyter_notebook_config.py`, GPU on Jupyter/code-server pods

## Row (for table)

| JupyterHub / Zero-to-JupyterHub (Z2JH); Kubeflow Notebooks; DIY Jupyter Deployments; Docker/Compose Jupyter stacks; code-server / VS Code ML pods; RStudio Server DIY; Amazon SageMaker Studio; Google Vertex AI Workbench / Colab Enterprise; Azure ML compute instances/notebooks; Databricks notebooks; Domino Data Lab / Anaconda Enterprise; Binder / repo2docker; shared bastion / SSH GPU boxes | Workbenches | jupyterhub / jupyterhub_config.py / c.KubeSpawner. / zero-to-jupyterhub / jupyterhub/jupyterhub Helm / singleuser.image; kind: Notebook kubeflow.org/v1; DIY Deployment+Route+PVC jupyter/*-notebook / start-notebook; docker-compose Jupyter / JUPYTER_ENABLE_LAB / :8888 / /home/jovyan; code-server / codercom/code-server; rstudio-server / rocker/rstudio; SageMaker Studio / CreateDomain / create-notebook-instance; Vertex Workbench / gcloud notebooks / Colab; azure.ai.ml compute instance; Databricks notebooks; Domino / Anaconda Enterprise; mybinder.org / repo2docker; *.ipynb / .jupyter/ / NOTEBOOK_ARGS / ServerApp.* |
