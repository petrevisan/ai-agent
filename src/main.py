import os
import dotenv

dotenv.load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

print(OPENAI_API_KEY)

def main():
    print("Hello from ai-agent!")


if __name__ == "__main__":
    main()
