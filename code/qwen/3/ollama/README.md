### 安装 ollama
```shell
curl -fsSL https://ollama.com/install.sh | sh
```


### 配置ollama环境

#### cpu 加载/ gpu 加载 （自动识别）
```shell
export OLLAMA_HOST="0.0.0.0:6006"

export OLLAMA_MODELS=/root/autodl-tmp/models

echo $OLLAMA_HOST
```

#### GPU加载 单卡/多卡
```shell
export OLLAMA_HOST="0.0.0.0:6006"
export OLLAMA_GPU_LAYER=cuda
export OLLAMA_NUM_GPU=4
export CUDA_VISIBLE_DEVICES=0,1,2,3
export OLLAMA_SCHED_SPREAD=1
export OLLAMA_KEEP_ALIVE=-1
export OLLAMA_MODELS=/root/autodl-tmp/models
echo $OLLAMA_HOST
```


### 制作ModelFile文件
```text
FROM /root/autodl-tmp/Qwen/qwen3_8b_q8_0.gguf

# set the temperature to 0.7 [higher is more creative, lower is more coherent]
PARAMETER temperature 0.7
PARAMETER top_p 0.8
PARAMETER repeat_penalty 1.05
TEMPLATE """{{ if .System }}<|im_start|>system
{{ .System }}<|im_end|>
{{ end }}{{ if .Prompt }}<|im_start|>user
{{ .Prompt }}<|im_end|>
{{ end }}<|im_start|>assistant
{{ .Response }}<|im_end|>"""
# set the system message
SYSTEM """
You are a helpful assistant.
"""
```

### 运行
```shell
ollama serve

ollama create midori --file ./ModelFile

ollama run midori
```