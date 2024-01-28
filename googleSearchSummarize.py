from langchain import GoogleSearchAPIWrapper

from chains import chain_create
from googleSearch import google_search, create_tool

if __name__ == "__main__":
    search = GoogleSearchAPIWrapper()
    summarize_chain = chain_create(
        input_variables=["query"],
        template="Write a summary of the following text: {query}"
    )
    summarize_agent = google_search(
        tools=[
            create_tool(
                name="Search",
                func=search,
                description="useful for finding information about recent events"
            ),
            create_tool(
                name='Summarizer',
                func=summarize_chain,
                description='useful for summarizing texts'
            )
        ]
    )
    response = summarize_agent("What's the latest football matches in 2024? Then please summarize the results.")
    print(response['output'])