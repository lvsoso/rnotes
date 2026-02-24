import os
from dotenv import load_dotenv
load_dotenv()

import pandas as pd
import numpy as np
import giskard
from giskard.rag import KnowledgeBase, generate_testset
from langchain_huggingface import HuggingFaceEmbeddings

# 1. 辅助函数：拼接 LiteLLM ID
def build_litellm_model_id(model_id: str, provider: str | None) -> str:
    """为 LiteLLM 拼接 provider/model。"""
    if provider and "/" not in model_id:
        return f"{provider}/{model_id}"
    return model_id

# 2. 加载 LLM 配置 (复用 SCAN_LLM 逻辑，或者直接用 LLM_MODEL_ID)
def load_scan_llm_config() -> tuple[str, str | None, str | None]:
    """读取用于 Giskard 生成测试集的 LLM 配置。"""
    # 优先使用 SCAN_ 前缀配置，如果没有则回退到普通配置
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

# 3. 加载 Embedding 配置 (本地 HuggingFace)
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

# 4. 示例数据（增加样本数量，避免降维时矩阵规模过小）
df = pd.DataFrame({
    "samples": [
        "Giskard is a great tool for testing and evaluating LLMs.",
        "Giskard Hub offers a comprehensive suite of tools for testing and evaluating LLMs.",
        "Giskard was founded in France by ex-Dataiku employees.",
        "Giskard helps data teams evaluate and monitor AI applications in production.",
        "You can use Giskard to automatically generate tests for LLM agents.",
        "RAGET is Giskard's toolkit for evaluating RAG systems using generated questions.",
        "Giskard integrates with popular LLM providers via LiteLLM.",
        "The Giskard SDK can be used locally or in CI pipelines.",
        "Giskard supports both traditional ML models and LLM-based applications.",
        "The Giskard Hub provides a UI to explore tests and evaluation results."
    ]
})

# 5. 构建知识库
knowledge_base = KnowledgeBase.from_pandas(
    df, 
    columns=["samples"],
    embedding_model=HuggingFaceEmbeddingWrapper(embeddings)
)

# 6. 生成测试集
output_path = os.path.join(os.path.dirname(__file__), "my_testset.jsonl")
print(f"Generating testset using LLM: {giskard_llm_model_id}")
testset = generate_testset(
    knowledge_base,
    num_questions=60,
    language='en',
    agent_description="A customer support agent for company X"
)

testset.save(output_path)
print(f"Testset saved to {output_path}")
