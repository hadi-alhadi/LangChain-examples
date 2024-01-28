from dotenv import load_dotenv
import os
from langchain.llms import OpenAI
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import DeepLake
from langchain.chains import RetrievalQA
from langchain.agents import initialize_agent, Tool
from langchain.agents import AgentType

load_dotenv()
os.environ['OPENAI_API_KEY'] = os.environ.get('OPENAI_API_KEY')
os.environ['ACTIVELOOP_TOKEN'] = os.environ.get('ACTIVELOOP_TOKEN')
ActiveLoopOrgId = os.environ.get('ACTIVE_LOOP_ORG_ID')

def getDB(activeloopOrgId, datasetName):
    embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")
    my_activeloop_org_id = activeloopOrgId
    my_activeloop_dataset_name = datasetName
    dataset_path = f"hub://{my_activeloop_org_id}/{my_activeloop_dataset_name}"
    db = DeepLake(dataset_path=dataset_path, embedding_function=embeddings)
    return db

def createAgent(db):
    # instantiate the wrapper class for GPT3
    llm = OpenAI(model="gpt-3.5-turbo-instruct", temperature=0)

    # create a retriever from the db
    retrieval_qa = RetrievalQA.from_chain_type(
        llm=llm, chain_type="stuff", retriever=db.as_retriever()
    )

    # instantiate a tool that uses the retriever
    tools = [
        Tool(
            name="Retrieval QA System",
            func=retrieval_qa.run,
            description="Useful for answering questions."
        ),
    ]

    # create an agent that uses the tool
    agent = initialize_agent(
        tools,
        llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True
    )
    return agent


def createdDeepLakeDataset(activeloopOrgId, datasetName, texts, question):
    # instantiate the LLM and embeddings models
    llm = OpenAI(model="gpt-3.5-turbo-instruct", temperature=0)

    # create our documents
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    docs = text_splitter.create_documents(texts)

    # create Deep Lake dataset
    db = getDB(activeloopOrgId, datasetName)

    # add documents to our Deep Lake dataset
    db.add_documents(docs)

    # create agent
    agent = createAgent(db)

    response = agent.run(question)
    print(response)


if __name__ == "__main__":
    createdDeepLakeDataset(
        activeloopOrgId=ActiveLoopOrgId,
        datasetName="your-dataSet-name-here",
        texts=[
            "Albert Einstein was born in March 14, 1879",
            "Lionel Andres Messi was born in June 24, 1987"
        ],
        question="When was Einstein born?"
    )
