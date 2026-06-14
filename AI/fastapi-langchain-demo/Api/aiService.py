from functools import lru_cache

from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI

from message import CommunicateMessageModel
from setting import get_settings


@lru_cache
def getDeepSeekAgent():
    llm = ChatOpenAI(
        model="deepseek-chat",
        api_key=get_settings().DEEPSEEK_API_KEY,
        base_url="https://api.deepseek.com"
    )
    agent = create_agent(
        model=llm,
        tools=[],
        system_prompt="you are a helpful assistant"
    )

    return agent

def deepSeekInvoke(message: CommunicateMessageModel):
    agent = getDeepSeekAgent()

    return agent.invoke({
        "messages": [
            HumanMessage(content=message.content)
        ]
    })




