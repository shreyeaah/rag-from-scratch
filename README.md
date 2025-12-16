# RAG from Scratch 🧠📚

This repository documents my step-by-step learning journey of
**Retrieval-Augmented Generation (RAG)** — starting from basic
keyword similarity to a simple RAG pipeline.

The essence of RAG involves adding your own data (via a retrieval tool) to the prompt that you pass into a large language model. As a result, you get an output. That gives you several benefits:

You can include facts in the prompt to help the LLM avoid hallucinations
You can (manually) refer to sources of truth when responding to a user query, helping to double check any potential issues.
You can leverage data that the LLM might not have been trained on.

Components of a basic rag system:
a collection of documents (formally called a corpus)
An input from the user
a similarity measure between the collection of documents and the user input

steps:
Receive a user input
Perform our similarity measure
Post-process the user input and the fetched document(s)



## Learning Path
1. Corpus & similarity basics
3. Keyword-based retrieval (Jaccard)
4. TF-IDF retrieval
5. Embedding-based retrieval
6. End-to-end mini RAG pipeline

