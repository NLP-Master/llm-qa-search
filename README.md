# Question answering using embeddings-based search

GPT excels at answering questions, but only on topics it remembers from its training data.  In this lab, the seach-ask method is used to answer questions using private data.

1. Search: search your library of text for relevant text sections.
2. Ask: insert the retrieved text sections into a message to ChatGPT and ask it the question

To complete this lab, you will need to set up an OpenAI API account and set up your development enviroment. Here's a link to the [QuickStart](https://platform.openai.com/docs/quickstart?context=python). Pay special attention to step 2 - set up your API key.

Python libraries used in this lab:

- [PyPDF](https://pypdf.readthedocs.io/en/stable/)
- [python-docx](https://python-docx.readthedocs.io/en/latest/)
- [LangChain](https://www.langchain.com)
- [LangChain OpenAI](https://python.langchain.com/docs/integrations/llms/openai/)
- [LangChain Community](https://api.python.langchain.com/en/latest/community_api_reference.html)
- [FAISS](https://github.com/facebookresearch/faiss)
