#!/usr/bin/env python3

# pip install openai
#

import openai
import os
# from IPython.display import display, Markdown, Latex, HTML, JSON

from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())  # store the result of last evaluation (expresion) in the interpreter

openai.api_key = os.getenv("OPENAI_API_KEY")
# openai.api_key = ""

# class Test:
#     def __init__(self):
#         self.name = "datacamp"
#         self._num = 7
# g = Test()

# print(g.name)
# print(g._num)

#env
# pip list

# Chat completion API https://platform.openai.com/docs/guides/gpt/chat-completions-api

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model = model,
        messages = messages,
        temperature = 0,)  #,???
    return response.choices[0].message.content


if __name__ == '__main__':
    print("hello world") 
    text = get_completion("What is the capital of France?")
    print(text)

    message = [{"role": "system", "content": "You are a python developer."}, 
                {"role": "user", "content": "What is the name of the first class in python?"}]
    response = get_completion(message, temperature=0)
    print(response)
    
    
    # display(HTML(response))
    # display(Markdown(response))

    # review = f""" """
    # sentiment = f""" """
    # prompt f""" customer reiew: {review}, sentiment: {sentiment}  """"

