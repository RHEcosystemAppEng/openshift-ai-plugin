# Kubeflow Spark Operator (KSO)

OpenShift AI component that runs **Apache Spark as Kubernetes-native workloads** via `SparkApplication` / `ScheduledSparkApplication` (`sparkoperator.k8s.io`) for large-scale ETL and feature engineering. Peers are DIY Spark-on-K8s submit paths, upstream/Google spark-operator installs outside RHOAI, orchestrator wrappers (Airflow/cron), and off-cluster Spark platforms teams use instead of (or before) adopting **Kubeflow Spark Operator (KSO)**.

## Peers

- **Apache Spark native K8s submit (DIY)** — `spark-submit --master k8s://…` / `spark.master=k8s://…` with `--deploy-mode cluster`, `spark.kubernetes.container.image*`, and hand-managed driver/executor pods (`spark-role=driver|executor`) without operator CRs
- **Google / GCP spark-on-k8s-operator (standalone)** — legacy `GoogleCloudPlatform/spark-on-k8s-operator` installs and docs still referenced as “Google spark-operator”
- **Upstream Kubeflow spark-operator (Helm / non-RHOAI)** — chart `spark-operator/spark-operator` from `https://kubeflow.github.io/spark-operator`, ns `spark-operator`, image `ghcr.io/kubeflow/spark-operator/…` outside DSC `kubeflowsparkoperator: Managed`
- **Airflow `SparkSubmitOperator` (to Kubernetes)** — DAG tasks shelling `spark-submit` against a k8s master URL instead of applying `SparkApplication`
- **CronJob / cron Spark without operator** — Kubernetes `CronJob` (or external cron) + custom image running spark-submit; no `ScheduledSparkApplication`
- **CI / GitOps wrappers around spark-submit** — Jenkins/GitHub Actions/Tekton/Argo steps that kubectl/oc-apply raw driver Pods or invoke spark-submit against the OpenShift API
- **Databricks Spark jobs** — Databricks Jobs / Spark clusters / Jobs API (off-cluster managed Spark)
- **Amazon EMR / AWS Glue Spark** — EMR steps, Glue Spark jobs, EMR-on-EKS without Kubeflow SparkApplication CRs
- **Google Dataproc / Azure Synapse (Spark)** — managed cloud Spark services as the batch engine
- **YARN / Hadoop / Spark Standalone / Mesos** — classic `--master yarn` / standalone cluster managers (not Kubernetes-native operator lifecycle)

**Not peers (adjacent catalog jobs):** Distributed Workloads (KubeRay, Training Operator) for Ray/PyTorch/TF GPU training; Workbenches / single-node pandas; Feature Store (Feast) as the store itself; Data Science Pipelines as the orchestrator (may *call* Spark); Flink / Beam / Dask operators (different engines/CRDs).

## Detection aliases

- DIY spark-submit k8s: `spark-submit --master k8s://`, `spark.master=k8s://`, `--deploy-mode cluster`, `spark.kubernetes.container.image`, `spark.kubernetes.driver.container.image`, `spark.kubernetes.executor.container.image`, `spark.kubernetes.authenticate.`, pod labels `spark-role=driver` / `spark-role=executor` without `sparkoperator.k8s.io`
- Google spark-operator standalone: `GoogleCloudPlatform/spark-on-k8s-operator`, “GCP spark operator”, legacy GoogleCloudPlatform Helm/manifests
- Upstream Kubeflow spark-operator: Helm repo `kubeflow.github.io/spark-operator`, chart `spark-operator/spark-operator`, `ghcr.io/kubeflow/spark-operator`, ns `spark-operator`, GitHub `kubeflow/spark-operator` (non-RHOAI path)
- Airflow SparkSubmitOperator: `airflow.providers.apache.spark.operators.spark_submit.SparkSubmitOperator`, `SparkSubmitOperator(`, `conn_id=` spark-k8s, DAGs calling spark-submit to k8s
- Cron without operator: `kind: CronJob` + spark-submit image/command; shell cron wrapping `spark-submit`; schedule comments without `ScheduledSparkApplication` / `spec.schedule`
- CI/GitOps submit wrappers: pipeline steps `spark-submit` + OpenShift API; oc/kubectl apply of driver Pods; Flux/Argo applying non-CR Spark manifests
- Databricks: Databricks Jobs API, `databricks` spark clusters, notebook/job Spark configs (off-cluster)
- EMR / Glue: `aws emr`, EMR step configs, Glue Spark ETL jobs, EMR-on-EKS
- Dataproc / Synapse: `gcloud dataproc`, Azure Synapse Spark pools
- Classic cluster managers: `--master yarn`, Spark Standalone master URL, Mesos master (off-K8s)
- Need-for-KSO app markers: `pyspark`, `SparkSession`, `spark.sql`, cluster-scale ETL/feature jobs aimed at OpenShift; desire for GitOps `SparkApplication` / cron Spark / Prometheus monitoring

## Row (for table)

| Apache Spark native k8s submit (DIY spark-submit --master k8s://); Google/GCP spark-on-k8s-operator standalone; upstream Kubeflow spark-operator Helm (non-RHOAI); Airflow SparkSubmitOperator to k8s; CronJob/cron Spark without ScheduledSparkApplication; CI/GitOps spark-submit wrappers; Databricks Spark jobs; Amazon EMR / AWS Glue Spark; Google Dataproc / Azure Synapse Spark; YARN / Spark Standalone / Mesos | Kubeflow Spark Operator (KSO) | spark-submit --master k8s://, spark.master=k8s://, spark.kubernetes.container.image, spark-role=driver\|executor (no sparkoperator.k8s.io); GoogleCloudPlatform/spark-on-k8s-operator; Helm kubeflow.github.io/spark-operator, ghcr.io/kubeflow/spark-operator, ns spark-operator; Airflow SparkSubmitOperator; CronJob + spark-submit; CI/Tekton/Argo spark-submit wrappers; Databricks Jobs; aws emr / Glue Spark; gcloud dataproc / Synapse Spark pools; --master yarn / Standalone / Mesos; pyspark SparkSession cluster ETL on OpenShift |
