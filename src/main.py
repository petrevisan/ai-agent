import os
import dotenv
from langchain_community.chat_models import ChatOpenAI

dotenv.load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
llm = ChatOpenAI(model="gpt-4o-mini", api_key=OPENAI_API_KEY)


def main():
    response = llm.invoke("Quanto é 2 + 2?")
    print(response.content)


if __name__ == "__main__":
    main()
