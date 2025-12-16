
# Keyword-Based Retrieval using Jaccard Similarity

This module demonstrates a **basic document retrieval mechanism** using
**Jaccard similarity**, one of the simplest similarity metrics.

The purpose of this step is to understand **how retrieval works at a fundamental level**


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

### What is this?

* This list of sentences acts as a **knowledge base**
* Each sentence is treated as an individual **document**
* In real-world RAG systems, documents can be:

  * PDFs
  * Web pages
  * Research papers
  * Medical or technical guidelines

Here, a small and simple corpus is used to clearly demonstrate the retrieval logic.

---

## 2. Jaccard Similarity

Jaccard similarity measures how similar two sets are.

### Formula:

```
Jaccard Similarity = |Intersection| / |Union|
```

Where:

* **Intersection** → words common to both texts
* **Union** → all unique words across both texts

The score ranges from **0 to 1**:

* `0` → no overlap
* `1` → identical sets of words

---

## 3. Similarity Function Implementation

```python
def jaccard_similarity(query, document):
    query = query.lower().split(" ")
    document = document.lower().split(" ")
    intersection = set(query).intersection(set(document))
    union = set(query).union(set(document))
    return len(intersection) / len(union)
```

### Step-by-step explanation:

1. Convert both the query and document to lowercase
2. Split them into individual words (tokens)
3. Convert token lists into sets
4. Compute:

   * Common words (intersection)
   * Total unique words (union)
5. Return the Jaccard similarity score

---

## 4. Querying the Corpus

```python
query = "I want to enjoy nature"

for doc in corpus_of_documents:
    score = jaccard_similarity(query, doc)
    print(f"{score:.2f} → {doc}")
```

### What this does:

* Compares the query against **every document** in the corpus
* Calculates similarity scores
* Prints the relevance score for each document

This simulates a basic **retrieval step** in a RAG pipeline.

---

## 5. Example Output

```
0.07 → Take a leisurely walk in the park and enjoy the fresh air.
0.00 → Visit a local museum and discover something new.
0.00 → Attend a live music concert and feel the rhythm.
0.00 → Go for a hike and admire the natural scenery.
...
```

A non-zero score indicates at least one common word between the query and the document.

---

## 6. Observations

* Documents with shared keywords score higher
* Exact word matching is required
* No semantic understanding is involved

For example:

* `"nature"` ≠ `"natural"`
* `"walk"` ≠ `"hike"`

This explains why some intuitively relevant documents may still receive a score of `0.00`.

---

## 7. Limitations of Keyword-Based Retrieval

This approach has several limitations:

* No semantic or contextual understanding
* Sensitive to wording, tense, and plural forms
* Cannot handle synonyms or paraphrasing
* Performs poorly on real-world, complex text

Because of these limitations, modern RAG systems use **vector embeddings** instead of raw keywords.

---

## 8. Why This Step Matters in RAG

This implementation helps build intuition about:

* What a **corpus** is
* How **retrieval** works
* Why naive keyword matching fails
* The motivation for TF-IDF and embedding-based retrieval



---
<img width="935" height="345" alt="Screenshot 2025-12-16 204027" src="https://github.com/user-attachments/assets/19e39af7-aa95-479b-81d5-7c3224c09a6b" />



---

```

---


```
