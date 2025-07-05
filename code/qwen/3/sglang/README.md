### 环境

```shell
pip install vllm

pip install sglang orjson torchao

pip install sgl_kernel
```

### 非思考模式

```shell
python -m sglang.launch_server --model-path Qwen/Qwen3-8B --port 6006 --reasoning-parser qwen3
```

### 思考模式
```shell
python -m sglang.launch_server --model-path Qwen/Qwen3-8B --port 6006
```

### demo
```shell
python demo.py
```
