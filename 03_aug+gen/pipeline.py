import requests
import json

# Knowledge base
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

def jaccard_similarity(query, document):
    query = query.lower().split()
    document = document.lower().split()
    intersection = set(query).intersection(set(document))
    union = set(query).union(set(document))
    return len(intersection) / len(union)

def return_response(query, corpus):
    similarities = []
    for doc in corpus:
        similarity = jaccard_similarity(query, doc)
        similarities.append(similarity)
    return corpus[similarities.index(max(similarities))]

user_input = "I don't like to hike"
relevant_document = return_response(user_input, corpus_of_documents)

prompt = f"""
You are a bot that makes recommendations for activities.
You answer in very short sentences and do not include extra information.

This is the recommended activity:
{relevant_document}

The user input is:
{user_input}

Compile a recommendation to the user ased on the recommended activity and the user input.
"""

url = "http://localhost:11434/api/generate"
data = {
    "model": "llama3.2",
    "prompt": prompt
}

response = requests.post(url, json=data, stream=True)

full_response = []

for line in response.iter_lines():
    if line:
        decoded = json.loads(line.decode("utf-8"))
        #print(decoded)
        if "response" in decoded:
          full_response.append(decoded["response"])

print("".join(full_response))
