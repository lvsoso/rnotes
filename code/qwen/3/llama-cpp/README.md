### 下载 llama.cpp
```shell
git clone https://github.com/ggerganov/llama.cpp
```

### 配置llama.cpp环境
```shell
cd llama.cpp

pip install -r requirements.txt

mkdir build

sudo apt-get update

sudo apt-get install make cmake gcc g++ locate

cmake -B build -DGGML_CUDA=ON -DGGML_CUDA_ENABLE_UNIFIED_MEMORY=1 -DLLAMA_CURL=OFF

cmake --build build --config Release -j8

cd build

make install

```

### 获取gguf格式的模型

这里--outtype是输出类型，代表含义：

q2_k：特定张量（Tensor）采用较高的精度设置，而其他的则保持基础级别。
q3_k_l、q3_k_m、q3_k_s：这些变体在不同张量上使用不同级别的精度，从而达到性能和效率的平衡。
q4_0：这是最初的量化方案，使用 4 位精度。
q4_1 和 q4_k_m、q4_k_s：这些提供了不同程度的准确性和推理速度，适合需要平衡资源使用的场景。
q5_0、q5_1、q5_k_m、q5_k_s：这些版本在保证更高准确度的同时，会使用更多的资源并且推理速度较慢。
q6_k 和 q8_0：这些提供了最高的精度，但是因为高资源消耗和慢速度，可能不适合所有用户。
fp16 和 f32: 不量化，保留原始精度。

```shell
# 如果不量化，保留模型的效果
python convert_hf_to_gguf.py /root/autodl-tmp/Qwen/Qwen3-8B --outtype f16 --verbose --outfile /root/autodl-tmp/Qwen/qwen3_8b_f16.gguf

# 如果需要量化（加速并有损效果），直接执行下面脚本就可以
python convert_hf_to_gguf.py /root/autodl-tmp/Qwen/Qwen3-8B --outtype q8_0 --verbose --outfile /root/autodl-tmp/Qwen/qwen3_8b_q8_0.gguf
```

### 与模型对话
```shell
./bin/llama-cli -m /root/autodl-tmp/Qwen/qwen3_8b_q8_0.gguf -cnv --n-gpu-layers 2000
```

### 开放api接口
-ts:指定n张gpu的分配比例
```shell
./bin/llama-server -m /root/autodl-tmp/Qwen/qwen3_8b_q8_0.gguf --port 6006 --n-gpu-layers 2000 -ts 1,1,1,1
```
