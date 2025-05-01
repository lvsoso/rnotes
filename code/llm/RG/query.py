import json

import numpy as np
from faiss import IndexFlatL2
from google.generativeai.types import HarmCategory, HarmBlockThreshold
import google.generativeai as genai


def load_data(chunk_path, emb_path):
    with open(chunk_path, "rt", encoding="UTF-8") as fp:
        chunks = json.load(fp)
    key_emb: np.ndarray = np.load(emb_path)
    vectors = IndexFlatL2(key_emb.shape[1])
    vectors.add(key_emb)

    return chunks, vectors


def get_query_emb(query_text: str):
    result = genai.embed_content(
                model="text-embedding-004",
                content=query_text)
    query_emb = result['embedding']
    return np.array([query_emb])


def build_prompt(q_emb, q_text, vectors: IndexFlatL2, value_chunks):
    dist, index = vectors.search(q_emb, k=20)
    print(f"Distance: {dist}")
    print(f"Indices: {index}")
    prompts = [value_chunks[i] for i in reversed(index[0])]
    prompts.append(f"问题：{q_text}")
    return "\n\n".join(prompts)


def create_chat(prompt):
    sys_prompt = "你现在是个专业的文件检索问答机器人，请根据文件内容的信息回答问题。"
    
    # 配置 Gemini 模型
    generation_config = {
        "temperature": 0.7,
        "top_p": 0.95,
        "top_k": 40,
    }
    
    safety_settings = {
        HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
    }
    
    model = genai.GenerativeModel(
        model_name="gemini-2.0-flash",
        generation_config=generation_config,
        safety_settings=safety_settings
    )
    
    chat = model.start_chat(history=[
        {"role": "user", "parts": [sys_prompt]}
    ])
    
    response = chat.send_message(prompt, stream=True)

    def stream_response():
        for chunk in response:
            if hasattr(chunk, "text"):
                print(end=chunk.text, flush=True)
        print()

    return stream_response


def main():
    genai.configure(api_key='')
    query_text = "请介绍这篇论文"
    chunks, vectors = load_data("data/chunks.json", "data/embs.npy")
    query_emb = get_query_emb(query_text)
    prompt = build_prompt(query_emb, query_text, vectors, chunks)
    stream_response = create_chat(prompt)

    print(f"问题：{query_text}\n回答：")
    stream_response()


if __name__ == "__main__":
    main()
