# LangChain-examples

This repository contains examples of using langChain, a Python library for working with various language models (LLMs). The examples showcase different use cases and functionalities of langChain.

## Project Overview

LangChain-examples provides a convenient and consolidated resource for developers interested in leveraging langChain. Whether you are a beginner looking to understand how to use langChain or an experienced developer seeking inspiration for your own projects, you'll find a variety of examples here to explore and reuse.

The examples cover a spectrum of use cases, demonstrating how to interact with language models, construct chains, incorporate memory, and utilize vector databases. Additionally, practical scenarios, such as using Deep Lake as a vector store, are included to offer real-world insights into implementing langChain in your projects.


## Installation and API keys
Let's install the required packages with the following command: pip install langchain==0.0.208 deeplake openai==0.27.8 tiktoken.

In order to access OpenAI's services, you must first obtain credentials by signing up on their website, completing the registration process, and creating an API key from your dashboard. This enables you to leverage OpenAI's powerful capabilities in your projects.

1. If you don't have an account yet, create one by going to OpenAI Platform. If you already have an account, skip to step 5.
2. Fill out the registration form with your name, email address, and desired password.
3- OpenAI will send you a confirmation email with a link. Click on the link to confirm your account.
4. Please note that you'll need to verify your email account and provide a phone number for verification.
5. Log in to OpenAI Platform.
6. Navigate to the API key section at API Keys.
7. Click "Create new secret key" and give the key a recognizable name or ID.


In order to use Deep Lake, you first have to register on the Activeloop website and redeem your API token. Here are the steps for doing it:

1. Sign up for an account on Activeloop's platform. You can sign up at Activeloop's website. After specifying your username, click on the “Sign up” button. You should now see your homepage.
2. You should now see a “Create API token” button at the top of your homepage. Click on it, and you’ll get redirected to the “API tokens” page. This is where you can generate, manage, and revoke your API keys for accessing Deep Lake.
3. Click on the "Create API token" button. Then, you should see a popup asking for a token name and an expiration date. Once you’ve set the token name and its expiration date, click on the “Create API token” button.
4. You should now see a green banner saying that the token has been successfully generated, along with your new API token, on the “API tokens” page.


## Environment Variables

Make sure to create a `.env` file in the root of the project and add your keys:

```env
OPENAI_API_KEY=your-api-key-goes-here
ACTIVELOOP_TOKEN=your-token-goes-here
```

## Running Examples
### Example 1: llm.py
#### Description:
This example demonstrates how to use langChain to interact with the OpenAI language model (LLM). It suggests a personalized workout routine based on a given text prompt.

#### How to Run:
- Set up the environment variable as described above.
- Run the following command in your terminal:
```python llm.py```

The program will output the result of the language model based on the provided text prompt.
Feel free to explore other examples in the repository for different use cases and functionalities.

### Example 2: memory.py
#### Description:
This example illustrates how to use langChain to create a conversation chain with memory. It uses the OpenAI language model and a conversation buffer memory to maintain context throughout the conversation.

#### How to Run:
- Set up the environment variable as described above.
- Run the following command in your terminal:
```python memory.py```

The program will simulate a conversation and display the conversation history.
Feel free to explore other examples in the repository for different use cases and functionalities.


### Example 3: chains.py
#### Description:
This example highlights LangChain's LLMChain, a powerful tool that combines components like PromptTemplate and language models (LLM or ChatModel) for efficient natural language processing. The LLMChain simplifies the process:
- Takes input variables.
- Uses PromptTemplate to format them into a prompt.
- Sends the prompt to the model.
- Parses the output with an output parser.

#### How to Run:
- Set up the environment variable as described above.
- Run the following command in your terminal:
```python chains.py```

The program will output the result of the language model based on the generated prompt.
Feel free to explore other examples in the repository for different use cases and functionalities.


### Example 4: deepLakeDataset.py
#### Description:
This example demonstrates how to create and interact with a Deep Lake dataset using langChain. It involves creating a Deep Lake dataset from provided texts, setting up a retrieval question-answer system, and querying the dataset for answers.

#### How to Run:
- Set up the environment variables as described above.
- Run the following command in your terminal:
```python deepLakeDataset.py```

The program will output the answer to the provided question based on the created Deep Lake dataset.


## Contributing
If you'd like to contribute to this project, please follow the standard GitHub flow: fork the repository, create a branch, make your changes, and submit a pull request.

## License
This project is licensed under the MIT License.

Copy this directly into your README.md file in your GitHub repository.