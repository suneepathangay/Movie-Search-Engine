## write the vectors to a sqlite databse with the embeddings 
from embedding import text_to_vector,cosine_simialrit
from sentence_transformers import SentenceTransformer,util
import sqlite3
import torch
import requests
import requests
import json
import re
from password import get_password



   


##using the pincone vector database and algoritshms we are going to search


def post_data(link):


    #link="https://myflixer.to/movie/polite-society-96739"

    password=get_password()

    result = re.split(r'[/\?]', link)[-1]
    result=re.split('-',result)
    id=result[-1]
    result.remove(id)
    title=' '.join(result)

    vector=list(map(float,text_to_vector(title)))



    url = "https://movies-0f8aa6e.svc.asia-southeast1-gcp-free.pinecone.io/vectors/upsert"
    headers = {
        "Content-Type": "application/json",
        "Api-Key": password
    }

    data = {
        "vectors": [
            {
                "id": id,
                "metadata": {"link":link},
                "values": vector  # Replace with your vector values
            }
        ],
        "namespace": ""
    }



    payload = json.dumps(data)


    response = requests.post(url, headers=headers, data=payload)

    # Check the response
    if response.status_code == 200:
        print("POST request successful!")
    else:
        print("POST request failed:", response.text)
    return 

def query_db(text):

    vector=list(map(float,text_to_vector(text)))
    passwrd=get_password()

    url = "https://movies-0f8aa6e.svc.asia-southeast1-gcp-free.pinecone.io/query"
    headers = {
        "Content-Type": "application/json",
        "Api-Key": passwrd
    }
    data = {
        "vector": vector,
        "topK": 5,
        "includeMetadata": True,
        "includeValues": True,
        "namespace": ""
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    response_data = response.json()
    
    return response_data




#post_data('https://myflixer.to/movie/the-final-say-97333')

val1=query_db("")
print(val1)