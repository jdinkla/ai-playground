"""
This script is a simple example of how to use the OpenAI API to create a chatbot.
"""
import logging
from openai import OpenAI
from utilities import init
from openai_utilities import MODELS, message

init()

client = OpenAI()
completion = client.chat.completions.create(
    model=MODELS[0],
    messages=[
        message("system", "You are crazy advertisement guru."),
        message(
            "user", 
            "Create three names that consist of two or more words for a brand selling fake alcohol!"),
        message(
            "assistant", "1. Faux Spirits\n2. Mocktail Makers\n3. Counterfeit Cocktails"),
        message("user", "More sophisticated and a little french, please.")
    ]
)

logging.debug(completion)
print(completion.choices[0].message.content)
