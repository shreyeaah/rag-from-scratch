# Simple Keyword-Based Retriever using Jaccard Similarity

This module implements a **basic keyword-based retrieval system** using
**Jaccard similarity** and returns the **most relevant document** from a small
knowledge base given a user query.

This step mimics the **retrieval phase** of a Retrieval-Augmented Generation (RAG)
pipeline without using embeddings or language models.

---

## 1. Knowledge Base (Corpus)

```python
corpus_of_documents = [
    "Take a leisurely walk in the park and enjoy the fresh air.",
    "Visit a local museum and discover something new.",
    "Attend a live music concert and feel the rhythm.",
    "Go for a hike and admire the natural scenery.",
    "Have a picnic with friends and share some laughs.",
    "Explore a new cuisine by dining at an ethnic restaurant.",
    "Take a yoga class and stretch your body and mind.",
    "Join a local sports league and enjoy some friendly competition.",
    "Attend a workshop or lecture on a topic you're interested in.",
    "Visit an amusement park and ride the roller coasters."
]
````

### What this represents

* A **knowledge base** consisting of short text documents
* Each sentence is treated as a **single document**
* In real RAG systems, this would typically be:

  * Articles
  * PDFs
  * Medical guidelines
  * Website content

---

## 2. Jaccard Similarity

Jaccard similarity is a **set-based similarity metric** defined as:

```
Similarity = (Number of common words) / (Total unique words)
```

It measures how much overlap exists between the words in the query and a document.

---

## 3. Similarity Function

```python
def jaccard_similarity(query, document):
    query = query.lower().split(" ")
    document = document.lower().split(" ")
    intersection = set(query).intersection(set(document))
    union = set(query).union(set(document))
    return len(intersection) / len(union)
```

### How it works

1. Converts both query and document to lowercase
2. Splits them into words (tokens)
3. Converts tokens into sets
4. Computes:

   * **Intersection** → common words
   * **Union** → all unique words
5. Returns a similarity score between `0` and `1`

---

## 4. Retrieving the Most Relevant Document

```python
def return_response(query, corpus):
    similarities = []
    for doc in corpus:
        similarity = jaccard_similarity(user_input, doc)
        similarities.append(similarity)
    return corpus_of_documents[similarities.index(max(similarities))]
```

### What this function does

* Computes similarity scores between the query and every document
* Stores all similarity values
* Selects the document with the **highest similarity score**
* Returns the most relevant document

This simulates a **Top-1 retrieval step** in a RAG pipeline.

---

## 5. User Interaction Example

```python
user_prompt = "What is a leisure activity that you like?"
user_input = "I like to hike"

print(return_response(user_input, corpus_of_documents))
```

### Output

```
Go for a hike and admire the natural scenery.
```

The system correctly retrieves the document containing the keyword **"hike"**.

---

## 6. Limitations

This approach has several important limitations:

* Relies on **exact keyword matching**
* No understanding of semantics or meaning
* `"nature"` ≠ `"natural"`
* `"walk"` ≠ `"hike"`
* Sensitive to phrasing and word forms

Because of these limitations, real-world RAG systems use **TF-IDF** or
**embedding-based similarity** instead of raw keyword overlap.

---

## 7. Why This Step Matters

This implementation helps build intuition about:

* How document **retrieval** works
* How similarity scoring selects relevant context
* Why naive approaches fail in real applications

This foundational understanding is essential before moving on to
embedding-based RAG systems.


---

```

