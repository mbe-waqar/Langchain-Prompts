from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

messages = [
    SystemMessage("Hello, how are you?"),
    HumanMessage("I'm good, thanks. How about you?")
]

result = model.invoke(messages)

messages.append(AIMessage(content=result.content))

print(messages)