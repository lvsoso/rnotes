import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, MessagesState, START, END
from langchain_core.messages import HumanMessage
from langfuse.langchain import CallbackHandler

# 加载环境变量
load_dotenv()

# 检查 Langfuse 环境变量是否设置
required_vars = ["LANGFUSE_PUBLIC_KEY", "LANGFUSE_SECRET_KEY", "LANGFUSE_HOST"]
missing_vars = [var for var in required_vars if not os.getenv(var)]

if missing_vars:
    print(f"警告: 缺少 Langfuse 环境变量: {', '.join(missing_vars)}")
    print("请确保在 .env 文件中设置了这些变量，或者直接在环境中设置。")
    # 为了演示目的，如果缺少环境变量，我们可以尝试让用户输入，或者直接报错
    # 这里我们只打印警告，让程序继续运行，但 Langfuse 可能无法工作
else:
    print("Langfuse 环境变量已检测到。")

# 初始化Langfuse CallbackHandler
# Langfuse v3 推荐使用环境变量自动配置
langfuse_handler = CallbackHandler()

# 初始化 LLM
# 使用环境变量中的配置，如果没有则使用默认值或提示错误
llm = ChatOpenAI(
    model=os.getenv("LLM_MODEL_ID", "gpt-3.5-turbo"),
    api_key=os.getenv("LLM_API_KEY"),
    base_url=os.getenv("LLM_BASE_URL"),
)

# 定义 Graph 状态和节点
def chatbot(state: MessagesState):
    """
    简单的聊天机器人节点，调用 LLM 生成回复
    """
    messages = state['messages']
    response = llm.invoke(messages)
    return {'messages': [response]}

# 构建 Graph
workflow = StateGraph(MessagesState)

# 添加节点
workflow.add_node("chatbot", chatbot)

# 添加边
workflow.add_edge(START, "chatbot")
workflow.add_edge("chatbot", END)

# 编译 Graph
app = workflow.compile()

# 运行 Graph 并集成 Langfuse
def run_demo():
    print("开始运行 LangGraph Demo with Langfuse...")
    
    input_message = HumanMessage(content="你好，请介绍一下你自己。")
    
    # 在 invoke 时传入 config，包含 callbacks
    # 注意：langfuse_handler 需要作为 callbacks 列表的一部分传入
    result = app.invoke(
        {"messages": [input_message]},
        config={"callbacks": [langfuse_handler]}
    )
    
    print("\nAI 回复:")
    print(result['messages'][-1].content)
    print("\nLangfuse 追踪已完成（如果配置正确）。")

if __name__ == "__main__":
    run_demo()
