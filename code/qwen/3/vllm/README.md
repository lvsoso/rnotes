### 环境配置
```shell
pip install vllm
pip install flash-attn --no-build-isolation
```

### 单卡
```shell
vllm serve Qwen3-8B --dtype auto --port 6006 --max_model_len 8784 --gpu_memory_utilization 0.8

Qwen3-8B：模型权重位置
dtype：数据类型，一般直接auto就可以了，低版本的显卡可能需要自己设置，如2080要设置为half
port：端口号
limit_mm_per_prompt image=4，默认是1，这样每次请求可以输入多张图片
max_model_len：最大的token长度，爆显存了就改小
gpu_memory_utilization：GPU最大利用率，爆显存了就改小，我现在一般设置为0.7-0.8 \
```

### 多卡
```shell
vllm serve Qwen3-8B --dtype half --port 6006 --tensor-parallel-size 2 --pipeline-parallel-size 2 --gpu-memory-utilization 0.7 --max_model_len 8784

tensor-parallel-size：模型的权重将被分割成n部分分布在GPU上。
pipeline-parallel-size：设置流水线并行的大小为k，意味着模型的不同层将被分布到k个GPU上。
保证n*k=卡的数量，正好等于您拥有的GPU数量。
```


### open-webui

```shell
pip install open-webui

vllm serve Qwen3-8B --dtype auto --port 5000 --max_model_len 8784 --gpu_memory_utilization 0.8
```

```shell
export HF_ENDPOINT=https://hf-mirror.com
export ENABLE_OLLAMA_API=False
export OPENAI_API_BASE_URL=http://127.0.0.1:5000/v1
export DEFAULT_MODELS="Qwen3-8B"

open-webui serve --port 6006
# http://localhost:8000
```

openai格式
```shell
pip install openai

python -m vllm.entrypoints.openai.api_server --served-model-name Qwen3-8B --model /root/autodl-tmp/Qwen/Qwen3-8B --dtype auto --port 6006 --max_model_len 8784 --gpu_memory_utilization 0.8
```

### 禁用思考格式
```shell
vllm serve Qwen3-8B --dtype auto --port 6006 --max_model_len 8784 --gpu_memory_utilization 0.8 --enable-reasoning --reasoning-parser deepseek_r1
```