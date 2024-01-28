from dotenv import load_dotenv
import os
from langchain.llms import OpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

load_dotenv()
os.environ['OPENAI_API_KEY'] = os.environ.get('OPENAI_API_KEY')


def memory():
    llm = OpenAI(model="gpt-3.5-turbo-instruct", temperature=0)
    return ConversationChain(
        llm=llm,
        verbose=True,
        memory=ConversationBufferMemory()
    )


if __name__ == "__main__":
    # The Memory
    conversation = memory()
    # Start the conversation
    conversation.predict(input="Tell me about yourself.")
    # Continue the conversation
    conversation.predict(input="What can you do?")
    conversation.predict(input="How can you help me with data analysis?")
    # Display the conversation
    print(conversation)
