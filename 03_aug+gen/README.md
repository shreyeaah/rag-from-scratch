
## Augmentation + Generation

This step upgrades the project from a **retrieval-only system** to a **true Retrieval-Augmented Generation (RAG) pipeline** by introducing a local Large Language Model (LLM).

---

### 1. Added a Local LLM via Ollama

Previously, the pipeline stopped after retrieving the most relevant document.

In this step:
- An **open-source LLM** is run **locally** using **Ollama**
- No external APIs or keys are required
- The model listens on:
```

[http://localhost:11434](http://localhost:11434)

````

To start the LLM, a separate terminal must be opened and kept running:

```bash
ollama run llama3.2
````

This terminal acts as a **local LLM server**, while the Python script acts as a client.

---

### 2. Prompt Augmentation Introduced

Instead of directly returning the retrieved document, it is now **injected into the prompt**:

```text
Retrieved document → Context for the LLM
User input          → User intent
```

The LLM receives both and generates a response that reasons over:

* The retrieved activity
* The user’s stated preference

This marks the transition from **retrieval** to **augmentation + generation**.

---

### 3. Handling Conflicting User Intent

In earlier steps, the system would blindly return the retrieved document.

Now, even if the user input conflicts with the retrieved context:

```text
User input: "I don't like to hike"
Retrieved document: "Go for a hike and admire the natural scenery."
```

The LLM:

* Does **not** rigidly repeat the retrieved activity
* Adjusts the recommendation based on user intent
* Produces a more natural and sensible response

This behavior is a direct result of **LLM reasoning**, not changes to the retriever.

---

### 4. Streaming Responses from the LLM

The LLM response is now **streamed token-by-token** from Ollama:

```python
response = requests.post(url, json=data, stream=True)
```

Each streamed chunk is checked safely:

```python
if "response" in decoded:
    full_response.append(decoded["response"])
```

This prevents errors caused by non-text metadata messages.

---

### 5. Architectural Shift

**Before:**

```
User Input → Retriever → Output
```

**Now:**

```
User Input
   ↓
Retriever
   ↓
Context
   ↓
Prompt Augmentation
   ↓
Local LLM (Ollama)
   ↓
Generated Response
```

This completes the **first full RAG loop** in the repository.

---
### an error i faced


When using Ollama’s streaming API, the response is not sent as a single block of text but as a stream of multiple JSON messages, and **not all of these messages contain generated text**. 
During generation, Ollama sends chunks with a `"response"` field that hold partial text, but once generation finishes it also sends **metadata-only messages** such as `{"done": true}` that do not include any text.
In the earlier (wrong) version of the code, every streamed chunk was assumed to contain a `"response"` key, so the code either failed with a `KeyError` or produced no output when it encountered these metadata-only chunks. 
The corrected version explicitly checks whether `"response"` exists in each decoded message before appending it, ensuring that only actual text tokens are collected while safely ignoring non-text control messages.


### Summary

This step introduces:

* Local LLM execution (Ollama)
* Prompt augmentation
* LLM-based reasoning
* Robust handling of conflicting user intent

No changes were made to the retriever logic itself — the improvement comes entirely from **generation**.

```
<img width="951" height="188" alt="image" src="https://github.com/user-attachments/assets/b3f9a7e7-e186-47f0-af3b-0453d515a54e" />
<img width="924" height="125" alt="image" src="https://github.com/user-attachments/assets/3ba68736-66e4-4086-b172-138c4f680ef7" />


