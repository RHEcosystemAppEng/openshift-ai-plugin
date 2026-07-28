# Distributed Workloads (KubeRay, Training Operator)

RHOAI infrastructure for **multi-node / multi-GPU ML training and data processing**: KubeRay (`RayCluster`/`RayJob`) and Kubeflow Training Operator (`PyTorchJob` and related CRs), with GPU-aware scheduling and Red Hat build of **Kueue** fair-share queues. Peers are DIY launchers, framework-native multi-device stacks, and non-RHOAI orchestrators teams use instead of (or before) adopting this catalog path.

## Peers

- DIY `torchrun` / `torch.distributed` — multi-process DDP/FSDP launched via SSH, hostfiles, or bare `torchrun --nnodes` without Kubernetes CRs
- Slurm / sbatch GPU partitions — on-prem HPC schedulers (`srun`, `sbatch`, `#SBATCH --gpus`) for multi-node training
- MPI / OpenMPI hostfile launches — `mpirun`/`mpiexec` + NCCL for multi-node ranks outside Training Operator
- DeepSpeed multi-node launcher — `deepspeed --num_gpus` / `--hostfile` + ZeRO (`ds_config.json`) as the orchestration layer
- Horovod — `horovodrun` / `hvd.init()` MPI/Gloo distributed training without KubeRay or PyTorchJob
- Ray standalone / Anyscale — `ray.init`, Ray Train `TorchTrainer`, or managed Anyscale clusters without RHOAI KubeRay/CodeFlare
- Hugging Face Accelerate — `accelerate launch` / `Accelerator()` multi-GPU/node without platform job CRs
- PyTorch Lightning multi-device — `pl.Trainer(strategy="ddp"|"fsdp"|"deepspeed"|"horovod")` as the only scale-out layer
- Upstream Kubeflow Training Operator / PyTorchJob — `kind: PyTorchJob` / `TFJob` / `MPIJob` on vanilla Kubeflow or DIY clusters (not RHOAI DSC `trainingoperator`)
- Upstream KubeRay on vanilla Kubernetes — `RayCluster`/`RayJob`/`RayService` outside OpenShift AI Managed Ray + Kueue
- Custom Job / StatefulSet Master+Worker — hand-rolled rank wiring, `MASTER_ADDR`/`WORLD_SIZE`, idle always-on GPU pools
- Amazon SageMaker distributed training — SageMaker Training jobs / `smdistributed` / torch distributed on SageMaker
- Google Vertex AI Custom Training — Vertex custom jobs / WorkerPoolSpecs for multi-replica GPU training
- Azure Machine Learning distributed jobs — Azure ML multi-node PyTorch/MPI training compute
- Volcano / generic batch JobSet DIY — Volcano Jobs or JobSet/LWS multi-pod sets used as training infra instead of Training Operator/KubeRay

## Detection aliases

- DIY torchrun / torch.distributed: `torchrun`, `torch.distributed.run`, `torch.distributed.init_process_group`, `DistributedDataParallel`/`DDP(`, `FullyShardedDataParallel`/`FSDP(`, `WORLD_SIZE`/`RANK`/`LOCAL_RANK`/`MASTER_ADDR`/`MASTER_PORT`, `NCCL_*`, `nproc_per_node`, `torchrun --nnodes`, SSH/hostfile multi-node scripts
- Slurm / HPC: `sbatch`, `srun`, `#SBATCH`, `SLURM_`, `scontrol`, GPU partition/`--gres=gpu`
- MPI: `mpirun`, `mpiexec`, `hostfile`, OpenMPI/MPICH, `OMPI_`, rank/slot host lists for training
- DeepSpeed: `import deepspeed`, `deepspeed.initialize(`, `ds_config.json`, `--deepspeed_config`, `"zero_optimization"`, `"stage": 1|2|3`, `deepspeed --num_gpus`, `deepspeed --hostfile`
- Horovod: `import horovod.torch`, `horovod.tensorflow`, `hvd.init()`, `hvd.DistributedOptimizer`, `horovodrun -np`, `horovodrun -H`
- Ray standalone / Anyscale: `from ray.train.torch import TorchTrainer`, `ScalingConfig(`, `ray.train.torch.prepare_model`, `ray.init`, `@ray.remote`, `anyscale`, Anyscale Cloud (no RHOAI CodeFlare/`redhat-ods` KubeRay)
- Accelerate: `accelerate launch`, `from accelerate import Accelerator`, `Accelerator()`, `FullyShardedDataParallelPlugin`, `accelerate config`
- Lightning: `pytorch_lightning`/`lightning.pytorch`, `pl.Trainer(`, `strategy="ddp"`, `strategy="fsdp"`, `strategy="deepspeed"`, `FSDPStrategy`, `DeepSpeedStrategy`
- Upstream Training Operator: `kind: PyTorchJob`, `apiVersion: kubeflow.org/v1`, `pytorchReplicaSpecs`, `TFJob`/`MPIJob`/`XGBoostJob`, `TrainingClient`, `kubeflow-training-operator` outside RHOAI DSC Managed
- Upstream KubeRay: `kind: RayCluster`/`RayJob`/`RayService`, `apiVersion: ray.io/v1`, `kuberay-operator` on non-RHOAI clusters
- DIY K8s Master/Worker: custom `Job`/`StatefulSet` with Master/Worker roles, manual `MASTER_ADDR`, always-on GPU Deployments for training
- SageMaker / Vertex / Azure ML: `sagemaker` TrainingJob/`smdistributed`, Vertex `CustomJob`/`WorkerPoolSpec`, Azure ML `PyTorchDistribution`/`MpiDistribution` multi-node
- Volcano / JobSet DIY: `volcano.sh`, `kind: Job` (Volcano), `kind: JobSet`, LeaderWorkerSet used as training scale-out

## Row for `Distributed Workloads (KubeRay, Training Operator)`

| DIY torchrun/torch.distributed (SSH/hostfile); Slurm/sbatch GPU partitions; MPI/OpenMPI hostfile launches; DeepSpeed multi-node launcher; Horovod/horovodrun; Ray standalone/Anyscale; Hugging Face Accelerate; PyTorch Lightning multi-device strategies; upstream Kubeflow Training Operator/PyTorchJob; upstream KubeRay on vanilla K8s; custom Job/StatefulSet Master+Worker; SageMaker distributed training; Vertex AI Custom Training; Azure ML distributed jobs; Volcano/JobSet DIY | Distributed Workloads (KubeRay, Training Operator) | torchrun / torch.distributed / DDP / FSDP / WORLD_SIZE / MASTER_ADDR / NCCL_* / --nnodes; sbatch / srun / SLURM_ / --gres=gpu; mpirun / hostfile / OpenMPI; deepspeed / ds_config.json / zero_optimization / --hostfile; horovod / hvd.init / horovodrun; Ray TorchTrainer / ScalingConfig / ray.init / anyscale; accelerate launch / Accelerator(); pl.Trainer strategy=ddp|fsdp|deepspeed; PyTorchJob / kubeflow.org/v1 / pytorchReplicaSpecs / TrainingClient; RayCluster / RayJob / ray.io/v1 (non-RHOAI); DIY Job/StatefulSet Master+Worker; SageMaker TrainingJob / smdistributed; Vertex CustomJob / WorkerPoolSpec; Azure ML PyTorchDistribution / MpiDistribution; volcano.sh / JobSet / LeaderWorkerSet |
