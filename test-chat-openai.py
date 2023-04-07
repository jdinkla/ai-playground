import os
import openai

model="gpt-3.5-turbo"

openai.api_key = os.getenv("OPENAI_API_KEY")
response = openai.ChatCompletion.create(
    model=model, 
    messages=[
        {"role": "system", "content": "You are crazy advertisement guru."},
        {"role": "user", "content": "Create three names that consist of two or more words for a brand selling fake alcohol!"},
        {"role": "assistant", "content": "1. Faux Spirits\n2. Mocktail Makers\n3. Counterfeit Cocktails"},
        {"role": "user", "content": "More sophisticated and a little french, please."},
    ])
print(response)