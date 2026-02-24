python -m vllm.entrypoints.openai.api_server \
--model /root/.cache/huggingface/Qwen/Qwen3-4B-Instruct-2507 \
--served-model-name Qwen3-4B-Instruct-2507 \
--tensor-parallel-size 1 \
--max-model-len 16384 \
--port 8000 \
--host 0.0.0.0 \
--gpu-memory-utilization 0.92 \
--enable-prefix-caching \
--dtype auto
