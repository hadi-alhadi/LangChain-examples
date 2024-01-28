from dotenv import load_dotenv
import os
from langchain.llms import OpenAI

load_dotenv()
os.environ['OPENAI_API_KEY'] = os.environ.get('OPENAI_API_KEY')

def LLMs(text):
    llm = OpenAI(model="gpt-3.5-turbo-instruct", temperature=0.9)
    print(llm(text))

if __name__ == "__main__":
    # LLMs
    text = "Suggest a personalized workout routine for someone looking to improve cardiovascular endurance and prefers outdoor activities."
    LLMs(text)