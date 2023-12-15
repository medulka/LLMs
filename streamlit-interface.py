#!usr/bin/env python3
"""
Task specific endpoints - deprecated
after: https://github.com/Aleph-Alpha/examples/blob/main/boilerplate/07_streamlit_mvp.py
"""
client_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxOTQ2MywidG9rZW5faWQiOjQwNzJ9.MsF_ZqRrFDRikisVrfD-8BWNwF60RGrWEXrBWjSrnjk"
model_of_choice = "luminous-extended"

from aleph_alpha_client import Client, Prompt, CompletionRequest, SemanticEmbeddingRequest, SemanticRepresentation
from typing import Sequence
import os
import math
import streamlit

client = Client(client_token)



# function for symmetric embeddings
def embed_sym(text:str) -> Sequence[float]:
    """
    Symmetric embedding function
    """
    request = SemanticEmbeddingRequest(
        prompt=Prompt.from_text(text),
        representation=SemanticRepresentation.Symmetric       
    )
    result = client.semantic_embed(request, model=model_of_choice)
    return result.embedding

# funtion for asymmetric embeddings of Queries
def embed_asym_query(text:str) -> Sequence[float]:
    """
    Asymmetric embedding function
    """
    request = SemanticEmbeddingRequest(
        prompt=Prompt.from_text(text),
        representation=SemanticRepresentation.Query
    )
    result = client.semantic_embed(request, model=model_of_choice)
    return result.embedding

# function for asymmetric embeddings of Documents
def embed_asym_documents(text:str) -> Sequence[float]:
    """
    Asymmetric embedding function
    """
    request = SemanticEmbeddingRequest(
        prompt=Prompt.from_text(text),
        representation=SemanticRepresentation.Document
    )
    result = client.semantic_embed(request, model=model_of_choice)
    return result.embedding

# function to calculate cosine similarity
def cosine_similarity(a: Sequence[float], b: Sequence[float]) -> float:
    dot_product = sum(x * y for x, y in zip(a, b))
    magnitude_a = math.sqrt(sum(x * x for x in a))
    magnitude_b = math.sqrt(sum(x * x for x in b))
    return dot_product / (magnitude_a * magnitude_b)

# funciton to complete a siumple text
def complete_text(text:str) -> str:
    request = CompletionRequest(
        prompt=Prompt.from_text(text),
        temperature=0.2,
        maximum_tokens=256,
        stop_sequences=["\n"]
    )
    result = client.complete(request, model=model_of_choice)
    return result.completions[0].completion

text = ("Enter a sentence to complete.")

# A minimal streamlit interface to access the model
streamlit.title("Luminous Streamlit Demo")
streamlit.write("This is a minimal streamlit interface to access the Aleph Alpha model.")
streamlit.markdown("### A minimal demo")
input_text = streamlit.text_input(text)

# buttom to complete the text
if streamlit.button("Complete"):
    completion = complete_text(input_text)
    streamlit.markdown(f"### Completion:")
    streamlit.write(completion)




