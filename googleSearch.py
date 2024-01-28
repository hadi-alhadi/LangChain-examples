from dotenv import load_dotenv
import os
from langchain.llms import OpenAI
from langchain.utilities import GoogleSearchAPIWrapper
from langchain.agents import initialize_agent, Tool
from langchain.agents import AgentType

from chains import chain_create

load_dotenv()

os.environ['OPENAI_API_KEY'] = os.environ.get('OPENAI_API_KEY')
os.environ['GOOGLE_API_KEY'] = os.environ.get('GOOGLE_API_KEY')
os.environ['GOOGLE_CSE_ID'] = os.environ.get('GOOGLE_CSE_ID')


def create_tool(name, func, description):
    return Tool(
        name=name,
        func=func.run,
        description=description
    )


def google_search(tools):
    llm = OpenAI(model="gpt-3.5-turbo-instruct", temperature=0)
    return initialize_agent(tools,
                            llm,
                            agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
                            verbose=True,
                            max_iterations=6)


if __name__ == "__main__":
    # Google Search via API.
    search = GoogleSearchAPIWrapper()

    search_agent = google_search(
        tools=[
            create_tool(
                name="google-search",
                func=search,
                description="useful for when you need to search google to answer questions about current events"
            )
        ]
    )
    response = search_agent("which films nominated for oscar 2024?")
    print(response['output'])
