# Custom Notebook Images

Administrator-published **workbench container images** that extend default OpenShift AI IDE environments with org-specific libraries, tools, OS packages, or pinned versions—built, pushed to a registry, and selected when creating workbenches (ImageStream / BYON import). Peers are DIY Jupyter/notebook image recipes, Hub/KubeSpawner custom singleuser images, CI-built notebook tags, and ad-hoc session package installs that teams use instead of (or before) adopting RHOAI Custom Notebook Images. Hosting/lifecycle peers belong under **Workbenches**, not here.

## Peers

- DIY `FROM jupyter/*-notebook` Dockerfiles — upstream Jupyter Docker Stacks bases (`minimal`/`scipy`/`pytorch`/`datascience-notebook`) plus `pip`/`mamba`/`apt` extras, without ODH `opendatahub.io/notebook-image` publish
- Hand-rolled `jupyter/docker-stacks` forks — org forks of docker-stacks with shared `requirements.txt` / `environment.yml` as the “blessed” notebook image
- JupyterHub / Z2JH `singleuser.image` — Helm `singleuser.image` / profile-list images for custom user environments (image need only; Hub hosting → Workbenches)
- KubeSpawner / DockerSpawner image overrides — `c.KubeSpawner.image`, `kubespawner_override.image`, per-profile custom notebook images
- CI-built notebook tags — `docker`/`podman`/`buildah` build+push of notebook/workbench tags to Quay/Harbor/ECR with no ImageStream BYON / dashboard Notebook images import
- Session `pip install` / setup cells — every notebook or shared “setup” cell installs critical libs because the base image is insufficient (candidate to bake into a custom image)
- Ad-hoc conda/mamba envs on shared hosts — team `environment.yml` / `conda create` on bastions or PVC home dirs instead of a registry-backed workbench image
- `repo2docker` / Binder image builds — git→image for ephemeral Jupyter envs (`jupyter-repo2docker`, BinderHub) used as the custom-env path
- Community workbench-images DIY — builds from `opendatahub-io-contrib/workbench-images` / `quay.io/opendatahub-contrib/workbench-images` consumed only via raw image pull, not BYON-labeled ImageStreams
- `FROM quay.io/modh/odh-*-notebook` without BYON — RHODS/RHOAI base Dockerfile + registry push but no `opendatahub.io/notebook-image` ImageStream / Settings → Notebook images import
- Micropipenv / Pipfile-locked DIY images — Pipfile/`micropipenv install` notebook Containerfiles maintained outside dashboard publish
- SageMaker custom notebook images / lifecycle configs — AWS Studio/notebook custom images or bootstrap scripts installing packages at start
- Vertex AI custom containers — custom container images for Vertex Workbench / User-Managed Notebooks
- Azure ML / Databricks custom environments — AML environment images or Databricks custom container/runtime for notebook clusters
- Domino / Anaconda Enterprise environments — platform “environments” / custom images as the org-standard notebook stack outside RHOAI

## Detection aliases

- DIY Jupyter stacks: `FROM quay.io/jupyter/` / `FROM jupyter/`, `jupyter/minimal-notebook`, `scipy-notebook`, `datascience-notebook`, `pytorch-notebook`, `start-notebook.sh` / `start-notebook.py` / `start-singleuser.sh` in Dockerfile
- docker-stacks forks: `jupyter/docker-stacks`, fork `requirements.txt`/`environment.yml` baked into notebook image, `COPY requirements.txt` + `pip install` in notebook Containerfile
- Hub singleuser image: `singleuser.image`, Helm `jupyterhub` values `singleuser:`, profileList custom image
- KubeSpawner overrides: `c.KubeSpawner.image`, `kubespawner_override`, `KubeSpawner.image`, `DockerSpawner.image`
- CI notebook tags: CI job `podman build`/`docker build`/`buildah bud` + push of `*-notebook` / `workbench` / `jupyter` tags; release tags like `notebook-v*` / `workbench-*`
- Session pip / setup cells: notebook cells `pip install`, `!pip install`, `%pip install`, shared `setup.ipynb` / “install dependencies” first cell; comments that base image lacks libs
- Ad-hoc conda: `conda env create`, `mamba install`, `environment.yml` on shared host/PVC without image build
- repo2docker / Binder: `repo2docker`, `jupyter-repo2docker`, `mybinder.org`, BinderHub build of notebook image
- Contrib workbench-images: `opendatahub-contrib/workbench-images`, `quay.io/opendatahub-contrib/workbench-images`
- modh base without BYON: `FROM quay.io/modh/odh-*-notebook` / `odh-pytorch-notebook` / `odh-generic-data-science-notebook` + push, missing `opendatahub.io/notebook-image: 'true'` ImageStream
- Micropipenv / Pipfile: `Pipfile`/`Pipfile.lock` + `micropipenv install` in notebook Dockerfile; `fix-permissions /opt/app-root` DIY without ImageStream labels
- Cloud custom envs: SageMaker custom image / lifecycle config; Vertex custom container; Azure ML environment Dockerfile; Databricks container runtime / custom Docker for notebooks; Domino environment / Anaconda Enterprise custom image
- RHOAI publish markers (target, not peer): ImageStream label `opendatahub.io/notebook-image: 'true'`, `app.kubernetes.io/created-by: byon`, annotations `opendatahub.io/notebook-image-name`, Settings → **Notebook images** → Import

## Row for `Custom Notebook Images`

| DIY FROM jupyter/*-notebook Dockerfiles; jupyter/docker-stacks forks; JupyterHub/Z2JH singleuser.image; KubeSpawner/DockerSpawner image overrides; CI-built notebook tags; session pip install / setup cells; ad-hoc conda/mamba on shared hosts; repo2docker/Binder image builds; opendatahub-contrib workbench-images DIY (raw pull); FROM quay.io/modh without BYON ImageStream; micropipenv/Pipfile DIY notebook images; SageMaker custom images/lifecycle configs; Vertex custom containers; Azure ML/Databricks custom environments; Domino/Anaconda Enterprise environments | Custom Notebook Images | FROM quay.io/jupyter/ / jupyter/*-notebook / start-notebook.sh|py / start-singleuser.sh; jupyter/docker-stacks + requirements.txt/environment.yml; singleuser.image / Helm singleuser: / profileList image; c.KubeSpawner.image / kubespawner_override / DockerSpawner.image; CI podman|docker|buildah build+push *-notebook/workbench tags; %pip / !pip install / setup.ipynb cells; conda env create / mamba / environment.yml on host; repo2docker / jupyter-repo2docker / mybinder.org; opendatahub-contrib/workbench-images / quay.io/opendatahub-contrib/workbench-images; FROM quay.io/modh/odh-*-notebook without opendatahub.io/notebook-image; Pipfile + micropipenv / fix-permissions DIY; SageMaker custom image/lifecycle; Vertex custom container; Azure ML env / Databricks custom runtime; Domino/Anaconda environments; (target) ImageStream opendatahub.io/notebook-image / byon / Notebook images Import |
