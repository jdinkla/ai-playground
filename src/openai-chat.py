from openai import ChatCompletion
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

response = ChatCompletion.create(
    model="gpt-3.5-turbo", 
    messages=[
        {"role": "system", "content": "You are crazy advertisement guru."},
        {"role": "user", "content": "Create three names that consist of two or more words for a brand selling fake alcohol!"},
        {"role": "assistant", "content": "1. Faux Spirits\n2. Mocktail Makers\n3. Counterfeit Cocktails"},
        {"role": "user", "content": "More sophisticated and a little french, please."},
    ])
logging.debug(response)
print(response["choices"][0]["message"]["content"])
