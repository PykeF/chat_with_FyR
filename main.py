import streamlit as st
from streamlit import sidebar
from langchain.memory import ConversationBufferMemory

from utils import get_chat_response

st.title("Chat with FyR")

with sidebar:
    openai_api_key = st.text_input("Please enter your OpenAI API key", type="password")
    st.markdown("[Get OpenAI API key](https://platform.openai.com/api-keys)")
    if st.button("🗑️ Clear History"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.session_state["messages"] = [{"role": "ai", "content": "Hi, my name is FyR, how can I help you?"}]
        st.experimental_rerun()

if "memory" not in st.session_state:
    st.session_state["memory"] = ConversationBufferMemory(return_messages=True)
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "ai", "content": "Hi, my name is FyR, how can I help you?" }]

for message in st.session_state["messages"]:
    st.chat_message(message["role"]).write(message["content"])

prompt = st.chat_input()
if prompt:
    if not openai_api_key:
        st.info("Please enter your OpenAI API Key")
        st.stop()
    st.session_state["messages"].append({"role": "human", "content": prompt})
    st.chat_message("human").write(prompt)

    with st.spinner("Freeze, don't move."):
        response = get_chat_response(prompt, st.session_state["memory"], openai_api_key)
    msg = {"role": "ai", "content": response}
    st.session_state["messages"].append(msg)
    st.chat_message("ai").write(response)