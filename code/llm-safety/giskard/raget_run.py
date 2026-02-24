from typing import List, Dict
import os
from dotenv import load_dotenv
load_dotenv()

import numpy as np
import pandas as pd
import giskard
from giskard.rag import evaluate, QATestset, KnowledgeBase
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_openai import ChatOpenAI


def build_litellm_model_id(model_id: str, provider: str | None) -> str:
    """为 LiteLLM 拼接 provider/model。"""
    if provider and "/" not in model_id:
        return f"{provider}/{model_id}"
    return model_id

def load_scan_llm_config() -> tuple[str, str | None, str | None]:
    """读取用于 Giskard 生成测试集的 LLM 配置。"""
    model_id = os.getenv("SCAN_LLM_MODEL_ID") or os.getenv("LLM_MODEL_ID", "")
    provider = os.getenv("SCAN_LITELLM_PROVIDER") or os.getenv("LITELLM_PROVIDER")
    api_key = os.getenv("SCAN_LLM_API_KEY") or os.getenv("LLM_API_KEY")
    base_url = os.getenv("SCAN_LLM_BASE_URL") or os.getenv("LLM_BASE_URL")
    return build_litellm_model_id(model_id, provider), api_key, base_url

giskard_llm_model_id, giskard_llm_api_key, giskard_llm_base_url = load_scan_llm_config()
giskard.llm.set_llm_model(
    giskard_llm_model_id,
    api_key=giskard_llm_api_key,
    base_url=giskard_llm_base_url,
)


llm = ChatOpenAI(
    model_name=os.getenv("LLM_MODEL_ID"),
    api_key=os.getenv("LLM_API_KEY"),
    base_url=os.getenv("LLM_BASE_URL"),
)

emb_model_name = os.getenv("EMBEDDING_MODEL_PATH", "sentence-transformers/all-MiniLM-L6-v2")
embeddings = HuggingFaceEmbeddings(model_name=emb_model_name)

class HuggingFaceEmbeddingWrapper(giskard.llm.embeddings.base.BaseEmbedding):
    def __init__(self, model) -> None:
        """保存 HuggingFaceEmbeddings 实例。"""
        self.model = model

    def embed(self, texts: list[str]) -> np.ndarray:
        """将文本列表转换为向量。"""
        return np.array(self.model.embed_documents(texts))

giskard.llm.set_embedding_model(HuggingFaceEmbeddingWrapper(embeddings))


def get_answer_from_agent(messages: List[Dict[str, str]]) -> str:
    """使用 LangChain 向量检索和 LLM 基于知识库回答问题。"""
    user_message = messages[-1]["content"] if messages else ""
    if not user_message.strip():
        return "I do not have enough information in the knowledge base to answer this question."

    query_vector = np.array(embeddings.embed_query(user_message))
    norms = np.linalg.norm(doc_vectors, axis=1) * np.linalg.norm(query_vector)
    norms = norms + 1e-8
    similarities = doc_vectors @ query_vector / norms

    top_indices = np.argsort(-similarities)[:3]
    context_parts = [df["samples"].iloc[i] for i in top_indices]
    context = "\n".join(f"- {c}" for c in context_parts)

    prompt = (
        "You are a helpful assistant that answers questions based only on the provided context.\n"
        "If the answer is not in the context, say that you do not know.\n\n"
        f"Context:\n{context}\n\n"
        f"Question: {user_message}\n"
        "Answer in a concise sentence."
    )

    try:
        response = llm.invoke(prompt)
        return response.content
    except Exception:
        return "I encountered an error while generating an answer."


testset = QATestset.load("my_testset.jsonl")

df = pd.DataFrame({
    "samples": [
        "Giskard is a great tool for testing and evaluating LLMs.",
        "Giskard Hub offers a comprehensive suite of tools for testing and evaluating LLMs.",
        "Giskard was founded in France by ex-Dataiku employees."
    ]
})

emb_model_name = os.getenv("EMBEDDING_MODEL_PATH", "sentence-transformers/all-MiniLM-L6-v2")
embeddings = HuggingFaceEmbeddings(model_name=emb_model_name)
doc_vectors = np.array(embeddings.embed_documents(df["samples"].tolist()))


knowledge_base = KnowledgeBase.from_pandas(
    df,
    columns=["samples"],
    embedding_model=HuggingFaceEmbeddingWrapper(embeddings),
)


def predict_fn(question: str, history=None) -> str:
    """A function representing your RAG agent."""
    messages = history if history else []
    messages.append({"role": "user", "content": question})

    answer = get_answer_from_agent(messages)

    return answer


report = evaluate(predict_fn, testset=testset, knowledge_base=knowledge_base)

# 小样本知识库下，UMAP + HDBSCAN 在绘制 topic 可视化时会报错；
# 这里将 knowledge_base 从报告中移除，仅保留数值指标与问答结果。
report._knowledge_base = None
report.save("my_testset_report")

# df_results = report.to_pandas()
# df_results.to_csv("my_testset_results.csv", index=False)
