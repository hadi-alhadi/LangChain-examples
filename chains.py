from dotenv import load_dotenv
import os
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

load_dotenv()
os.environ['OPENAI_API_KEY'] = os.environ.get('OPENAI_API_KEY')


def chain_create(input_variables, template):
    llm = OpenAI(model="gpt-3.5-turbo-instruct", temperature=0.9)
    prompt = PromptTemplate(
        input_variables=input_variables,
        template=template,
    )
    return LLMChain(llm=llm, prompt=prompt)


if __name__ == "__main__":
    # The Chains
    print(
        chain_create(
            input_variables=["product"],
            template="What is a good name for a company that makes {product}?"
        ).run("eco-friendly water bottles")
    )
