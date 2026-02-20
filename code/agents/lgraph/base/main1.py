# 安装：pip install streamlit
# 保存为 app.py，运行：streamlit run app.py

import streamlit as st

# 代码示例：Streamlit ChatBot 界面
def streamlit_chatbot_example():
    """Streamlit ChatBot 示例代码"""
    code = '''
import streamlit as st

# 页面配置
st.set_page_config(
    page_title="AI ChatBot",
    page_icon="🤖",
    layout="wide"
)

# 标题
st.title("🤖 AI ChatBot")
st.caption("基于 LangGraph 的智能对话助手")

# 侧边栏配置
with st.sidebar:
    st.header("⚙️ 配置")
    model = st.selectbox("模型", ["gpt-4", "gpt-3.5-turbo"])
    temperature = st.slider("Temperature", 0.0, 2.0, 0.7)
    max_tokens = st.number_input("Max Tokens", 100, 4000, 1000)

    st.divider()
    st.info("""
    💡 **使用说明**
    - 在下方输入框输入消息
    - 按 Enter 发送
    - 查看 AI 响应
    """)

# 初始化会话状态
if "messages" not in st.session_state:
    st.session_state.messages = []

# 显示对话历史
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# 用户输入
if prompt := st.chat_input("输入你的消息..."):
    # 添加用户消息
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    # 模拟 AI 响应
    with st.chat_message("assistant"):
        with st.spinner("思考中..."):
            import time
            time.sleep(1)
            response = f"[{model}] 收到消息: {prompt}"
            st.write(response)

    # 添加 AI 响应
    st.session_state.messages.append({"role": "assistant", "content": response})

# 清除历史按钮
if st.button("🗑️ 清除对话历史"):
    st.session_state.messages = []
    st.rerun()
    '''
    return code

# 显示示例代码
print("=== Streamlit ChatBot 示例 ===\n")
print(streamlit_chatbot_example())

print("\n\n=== Streamlit 核心组件 ===")
print("""
1. 文本组件:
   st.title("标题")
   st.header("头部")
   st.subheader("子标题")
   st.text("文本")
   st.markdown("**Markdown**")
   st.caption("说明文字")

2. 输入组件:
   st.text_input("输入框")
   st.text_area("文本区域")
   st.number_input("数字输入")
   st.slider("滑块")
   st.selectbox("下拉选择")
   st.multiselect("多选")
   st.checkbox("复选框")
   st.radio("单选")
   st.date_input("日期选择")

3. 聊天组件:
   st.chat_message("user")  # 用户消息
   st.chat_message("assistant")  # AI 消息
   st.chat_input("输入框")  # 聊天输入

4. 布局:
   st.sidebar  # 侧边栏
   st.columns(3)  # 多列布局
   st.tabs(["Tab1", "Tab2"])  # 标签页
   st.expander("可展开内容")

5. 数据展示:
   st.dataframe(df)  # 数据表格
   st.table(df)  # 静态表格
   st.json(data)  # JSON 数据
   st.line_chart(data)  # 折线图
   st.bar_chart(data)  # 柱状图

6. 状态管理:
   st.session_state.key = value  # 会话状态
   st.rerun()  # 重新运行

7. 辅助:
   st.spinner("加载中...")  # 加载动画
   st.success("成功！")  # 成功提示
   st.error("错误！")  # 错误提示
   st.warning("警告！")  # 警告提示
   st.info("信息")  # 信息提示
""")