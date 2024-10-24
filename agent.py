import os
from dotenv import load_dotenv

from langchain.agents.openai_assistant import OpenAIAssistantRunnable
from langchain.agents import AgentExecutor
from langchain.tools import Tool


load_dotenv()

# Access environment variables
ASSISTANT_ID = os.getenv("ASSISTANT_ID")


tools = []

agent = OpenAIAssistantRunnable(assistant_id=ASSISTANT_ID, as_agent=True)


agent_executor = AgentExecutor(agent=agent, tools=tools)
agent_executor.invoke({"content": "What's the weather in SF today divided by 2.7"})
