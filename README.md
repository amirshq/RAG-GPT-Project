# RAG_GPT Project

This repository showcases various applications of LLM chatbots and provides comprehensive insights into established methodologies for training and fine-tuning Language Models.

### List of projects:
- [x] [WebGPT](#WebGPT)
- [x] [RAG-GPT](#RAG-GPT)


## Project description:
<a id="WebGPT"></a>
<h3>WebGPT:</h3>
<p>
WebGPT is a powerful tool enabling users to pose questions that require internet searches. Leveraging GPT models:

* It identifies and executes the most relevant given Python functions in response to user queries. 
* The second GPT model generates responses by combining user queries with content retrieved from the web search engine. 
* The user-friendly interface is built using Streamlit.
* The web search supports diverse searches such as text, news, PDFs, images, videos, maps, and instant responses. 
* Overcoming knowledge-cutoff limitations, the chatbot delivers answers based on the latest internet content.

Libraries: [OpenAI](https://platform.openai.com/docs/models/overview) (It uses GPT model's function calling capability) - [duckduckgo-search](https://pypi.org/project/duckduckgo-search/) - [streamlit](https://docs.streamlit.io/)


</p>

<a id="RAG-GPT"></a>
<h3>RAG-GPT:</h3>
<p>
RAG GPT is a chatbot that enables you to chat with your documents (PDFs and Doc). The project works with two types of data:

1. With documents that you have vectorized and processed beforehand.
2. With documents that you upload while chatting with the model.

Libraries: [OpenAI](https://platform.openai.com/docs/models/overview) - [Langchain](https://python.langchain.com/docs/get_started/quickstart) - [ChromaDB](https://www.trychroma.com/) - [Gradio](https://www.gradio.app/guides/quickstart) 

</p>

<a id="DeepWebQuery"></a>
<h3>DeepWebQuery: Combining WebGPT and RAG-GPT:</h3>
<p>
DeepWebQuery is a chatbot that goes beyond typical internet searches. Built on the foundations of WebGPT and RAG-GPT, this project empowers users to delve into the depths of both general knowledge and specific URL content.

Key Features:</br>

* Intelligent Decision-Making: Our model intelligently decides whether to answer user queries based on its internal knowledge base or execute relevant Python functions.
* Dynamic Functionality: Identify and execute the most pertinent Python functions in response to user queries, expanding the scope of what the chatbot can achieve.
* Web-Integrated Responses: The second GPT model seamlessly combines user queries with content retrieved from web searches, providing rich and context-aware responses.
* Website-Specific Queries: When users inquire about a specific website, the model dynamically calls a function to load, vectorize, and create a vectordb from the site's content.
* Memory: DeepWebQuery boasts a memory feature that allows it to retain information about user interactions. This enables a more coherent and context-aware conversation by keeping track of previous questions and answers.
* Vectordb Interactions: Users can query the content of the vectordb by starting their questions with ** and exit the RAG conversation by omitting ** from the query. ** can trigger the third GPT model for RAG Q&A.
* Chainlit Interface: The user-friendly interface is built using Chainlit, enhancing the overall user experience.
* Diverse Search Capabilities: DeepWebQuery supports a variety of searches, including text, news, PDFs, images, videos, maps, and instant responses.
* Overcoming Knowledge-Cutoff Limitations: This chatbot transcends knowledge-cutoff limitations, providing answers based on the latest internet content and even allowing users to ask questions about webpage content.

</p>

<a id="Multimodal-ChatBot"></a>
<h3>Multimodal-ChatBot:</h3>
This project aims to develop a versatile chatbot capable of processing text and voice inputs, generating multimodal responses (text, voice, images), and conducting web searches to deliver accurate information. Additionally, the chatbot will be equipped to analyze documents and respond to related queries.

## Tutorial description:
<a id="LLM-function-calling-tutorial"></a>
<h3>LLM Function Calling Tutorial:</h3>
<p>
LLM-function-calling-tutorial
    showcases the capacity of GPT models to produce executable functions in JSON format. It illustrates this capability through a practical example involving the utilization of Python with the GPT model.

Libraries: [OpenAI](https://platform.openai.com/docs/models/overview)

</p>
<a id="LLM-function-calling-tutorial"></a>
<h2>Visualizing Text Vectorization:</h2>
<p>
Visualizing Text Vectorizationprovides a comprehensive visualization of text vectorization and demonstrates the power of vector search. It further explores the vectorization on both OpenAi `text-embedding-ada-002` and the open source `BAAI/bge-large-zh-v1.5` model.

Libraries: [OpenAI](https://platform.openai.com/docs/models/overview) - [HuggingFace](https://huggingface.co/BAAI/bge-large-zh-v1.5)



