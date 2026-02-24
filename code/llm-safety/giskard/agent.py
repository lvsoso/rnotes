import os
from dotenv import load_dotenv
load_dotenv()

from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import giskard
import pandas as pd
import numpy as np

def build_litellm_model_id(model_id: str, provider: str | None) -> str:
    """为 LiteLLM 拼接 provider/model。"""
    if provider and "/" not in model_id:
        return f"{provider}/{model_id}"
    return model_id


llm = ChatOpenAI(
    model_name=os.getenv("LLM_MODEL_ID"),
    api_key=os.getenv("LLM_API_KEY"),
    base_url=os.getenv("LLM_BASE_URL"),
)

def load_scan_llm_config() -> tuple[str, str | None, str | None]:
    """读取用于 Giskard 扫描的 LLM 配置。"""
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

# 2. 本地 embedding 模型
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

# 4. 知识库
pdf_path = "IPCC_AR6_SYR_LongerReport.pdf"
if not os.path.exists(pdf_path):
    raise FileNotFoundError(f"{pdf_path} 不存在，请放入当前目录")

docs = PyPDFLoader(pdf_path).load_and_split(
    RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
)
vectorstore = FAISS.from_documents(docs, embeddings)
retriever = vectorstore.as_retriever()

# 5. 问答链
prompt = ChatPromptTemplate.from_template(
    """You are the Climate Assistant.
Answer the question using only the following context:

{context}

Question: {question}"""
)
qa_chain = prompt | llm | StrOutputParser()

def answer(question: str) -> str:
    """根据检索上下文回答问题。"""
    docs = retriever.invoke(question)
    context = "\n\n".join(d.page_content for d in docs)
    return qa_chain.invoke({"question": question, "context": context})

# 6. Giskard 包装
def predict(df: pd.DataFrame) -> list[str]:
    """适配 Giskard 的批量预测输入输出。"""
    return [answer(q) for q in df["question"]]

model = giskard.Model(
    model=predict,
    model_type="text_generation",
    name="Climate QA",
    description="基于 IPCC 报告的气候问答模型",
    feature_names=["question"],
)

# 7. 扫描
if __name__ == "__main__":
    scan_results = giskard.scan(model, raise_exceptions=False)
    print(scan_results)
    scan_results.to_html("scan_results.html")
