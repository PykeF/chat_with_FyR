from langchain_openai import ChatOpenAI
from langchain.chains import ConversationChain
import os
from langchain.memory import ConversationBufferMemory

def get_chat_response(prompt, memory, openai_api_key):
    model = ChatOpenAI(model="gpt-3.5-turbo", openai_api_key=openai_api_key, openai_api_base="https://api.aigc369.com/v1")
    chain = ConversationChain(llm=model, memory=memory)
    response = chain.invoke({"input": prompt})
    return response["response"]


# memory = ConversationBufferMemory(return_messages=True)
# print(get_chat_response("Dame Lillard contract detail", memory, os.getenv("OPENAI_API_KEY")))
# print(get_chat_response("What is my previous question", memory, os.getenv("OPENAI_API_KEY")))
