# Model Customization (Fine-Tuning)

Tools and workflows for **adapting pre-trained generative LLMs** to domain/task data—SFT, LoRA/QLoRA, full fine-tuning, continual learning (OSFT), or preference/RL post-training—then checkpointing adapters or merged weights for serve. On OpenShift AI this is the **Training Hub + workbench / Kubeflow Trainer / pipeline** path on Distributed Workloads. Peers are DIY PEFT/TRL stacks, instruction-tuning frameworks, and ad-hoc SFT/alignment loops that teams run instead of (or before) catalog Model Customization.

## Peers

- Hugging Face PEFT (LoRA/QLoRA DIY) — `LoraConfig` / `get_peft_model` / `PeftModel` / `adapter_config.json` without Training Hub
- TRL SFT / preference / RLHF — `SFTTrainer`, `DPOTrainer`, `ORPOTrainer`, `PPOTrainer`, `GRPOTrainer`, `KTOTrainer` + preference `chosen`/`rejected` pairs
- Unsloth — `FastLanguageModel` / Unsloth+TRL LoRA/QLoRA speed path outside RH Training Hub LoRA backend
- Axolotl — YAML `datasets:` Alpaca/ShareGPT + `lora`/`qlora`/`fullfinetune` + `axolotl train`
- LLaMA-Factory — `llamafactory-cli train` / WebUI `--stage sft|dpo|ppo` / `--finetuning_type lora`
- torchtune — PyTorch-native SFT recipes / `SFTDataset` Alpaca/ShareGPT loops
- Hugging Face Transformers Trainer CausalLM SFT — ad-hoc `Trainer`/`TrainingArguments` on `AutoModelForCausalLM` instruction data (no PEFT/TRL framework brand)
- bitsandbytes QLoRA DIY — `BitsAndBytesConfig` / `load_in_4bit` / NF4 paired with PEFT train loops (training path, not serve-only compress)
- DeepSpeed ZeRO / FSDP / `torchrun` DIY SFT — multi-GPU CausalLM fine-tune scripts without RH Training Hub / TrainJob
- InstructLab / instructlab-training — synthetic instruction data → DIY or upstream InstructLab train (maps to Training Hub InstructLab-Training backend)
- OpenRLHF / verl — OSS RLHF/GRPO post-training stacks competing with TRL preference alignment
- NVIDIA NeMo / Megatron-LM fine-tune — NeMo SFT/PEFT recipes and Megatron distributed LLM train outside RHOAI Training Hub
- MS-SWIFT (ms-swift) — Alibaba Swift CLI/WebUI multi-method LLM fine-tune (LoRA/QLoRA/full/RLHF)
- LitGPT / Lightning Fabric fine-tune — Lightning AI LitGPT / Fabric SFT/LoRA cookbooks
- Classic alpaca-lora / QLoRA notebooks — standalone Alpaca/ShareGPT LoRA repos and Colab-style adapter bake-offs
- Upstream `training_hub` outside RHOAI packaging — bare `pip install training-hub` / cloned Training Hub cookbooks without workbench / TrainJob / `sft_pipeline` wrappers

**Not peers (adjacent catalog jobs):** **Distributed Workloads** alone (multi-node infra without LLM post-training algorithms); **AutoML** (tabular CSV search); **LLM Compressor** (PTQ/compress for serve, not domain weight adaptation); **LMEval** / **RAGAS** (eval only); prompt/RAG-only fixes with no `trainer.train` / adapters.

## Detection aliases

- PEFT DIY: `peft`, `LoraConfig`, `get_peft_model`, `PeftModel`, `TaskType.CAUSAL_LM`, `prepare_model_for_kbit_training`, `adapter_config.json`, `adapter_model.safetensors`, `merge_and_unload`, `target_modules=["q_proj"`
- TRL: `trl`, `SFTTrainer`, `SFTConfig`, `DPOTrainer`, `ORPOTrainer`, `PPOTrainer`, `GRPOTrainer`, `KTOTrainer`, `RewardTrainer`, `trl/scripts/sft.py`, `--use_peft`, preference fields `chosen`/`rejected`
- Unsloth: `unsloth`, `from unsloth import FastLanguageModel`, `FastLanguageModel.from_pretrained`, `use_gradient_checkpointing="unsloth"`, `push_to_hub_merged`
- Axolotl: `axolotl`, `axolotl train`, YAML `type: alpaca` / `sharegpt`, `qlora`, `fullfinetune`
- LLaMA-Factory: `llamafactory-cli`, `llamafactory`, `LLaMA-Factory`, `--stage sft`, `--stage dpo`, `--finetuning_type lora`
- torchtune: `torchtune`, `torch.distributed.checkpoint`, `SFTDataset`, torchtune recipes / `tune run`
- HF Trainer CausalLM SFT: `AutoModelForCausalLM` + `Trainer(` / `TrainingArguments` on instruction JSONL; `DataCollatorForCompletionOnlyLM`; Alpaca `instruction`/`input`/`output` or ShareGPT `conversations`
- bitsandbytes QLoRA (train): `BitsAndBytesConfig`, `load_in_4bit`, `bnb_4bit_quant_type="nf4"`, `bnb_4bit_use_double_quant` **with** PEFT/`trainer.train`
- DeepSpeed/FSDP DIY: `deepspeed`, `ZeRO`, `FullyShardedDataParallel`, `torchrun` wrapping CausalLM SFT without `training_hub` / `TrainJob`
- InstructLab: `instructlab`, `ilab`, `instructlab-training`, synthetic taxonomy → train chain
- OpenRLHF / verl: `OpenRLHF`, `openrlhf`, `verl`, `from verl`
- NeMo / Megatron: `nemo_toolkit`, `Megatron-LM`, NeMo `peft` / SFT recipes for LLMs
- MS-SWIFT: `ms-swift`, `swift.llm`, `swift sft`, `swift rlhf`
- LitGPT / Lightning: `litgpt`, `litgpt finetune`, Lightning Fabric LoRA/SFT
- Classic DIY: `alpaca-lora`, `qlora`, checkpoint dirs `*-lora` / `*-qlora` / `*-sft` / `*-dpo` / `adapter_*`
- Upstream Training Hub (non-RHOAI): `from training_hub import sft` / `osft` / `lora_sft` without RHOAI workbench / `kind: TrainJob` / `sft_pipeline` / `osft_pipeline`

## Row for `Model Customization (Fine-Tuning)`

| Hugging Face PEFT (LoRA/QLoRA DIY); TRL SFT/DPO/ORPO/PPO/GRPO/KTO; Unsloth; Axolotl; LLaMA-Factory; torchtune; HF Transformers Trainer CausalLM SFT; bitsandbytes QLoRA DIY; DeepSpeed ZeRO/FSDP/torchrun DIY SFT; InstructLab/instructlab-training; OpenRLHF/verl; NVIDIA NeMo/Megatron-LM fine-tune; MS-SWIFT; LitGPT/Lightning Fabric fine-tune; classic alpaca-lora/QLoRA notebooks; upstream training_hub outside RHOAI packaging | Model Customization (Fine-Tuning) | peft / LoraConfig / get_peft_model / adapter_config.json / merge_and_unload; trl / SFTTrainer / DPOTrainer / chosen|rejected; unsloth / FastLanguageModel; axolotl train / type: alpaca|sharegpt; llamafactory-cli / --stage sft|dpo / --finetuning_type lora; torchtune / SFTDataset / tune run; AutoModelForCausalLM + Trainer SFT; BitsAndBytesConfig / load_in_4bit + PEFT train; deepspeed / FSDP / torchrun DIY SFT; instructlab / ilab / instructlab-training; OpenRLHF / verl; nemo_toolkit / Megatron-LM peft; ms-swift / swift sft; litgpt finetune; alpaca-lora / *-lora|*-sft|adapter_*; training_hub sft/osft/lora_sft without TrainJob/sft_pipeline |
