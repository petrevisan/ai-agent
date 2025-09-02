import os
import dotenv
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain_core.prompts import ChatPromptTemplate
from langchain.agents import AgentExecutor, create_tool_calling_agent

@tool
def get_current_weather(city: str) -> str:
    "Busca o clima de uma cidade."
    return f"The weather in {city} is sunny"

def get_current_time(city: str) -> str:
    "Busca o horário de uma cidade."
    return f"The time in {city} is 10:00"

prompt = ChatPromptTemplate.from_messages([
    ("system", "Você é um assistente que ajuda com informações sobre clima."),
    ("human", "{input}"),
    ("placeholder", "{agent_scratchpad}"),  # ← Esta linha é obrigatória!
])

tools = [get_current_weather]


dotenv.load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY is not set")

llm = ChatOpenAI(model="gpt-4o-mini", api_key=OPENAI_API_KEY)

agent = create_tool_calling_agent(llm, tools, prompt)
executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

res = executor.invoke({"input": "Qual o clima de São Paulo? E qual o horário de São Paulo?"})
print(res["output"])


# if __name__ == "__main__":
#    main()
