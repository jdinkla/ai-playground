"""
Simple completion using OpenAI API
"""

import logging
from openai import OpenAI
from openai_utilities import MODELS
from utilities import init

init()

client = OpenAI()
response = client.completions.create(
    model="gpt-3.5-turbo-instruct",
    prompt="""
        Create a name for an AI consulting company that will lead us into a better and fairer future. 
        The name should not include 'solutions', 'tech' or 'consulting'.
        """,
    temperature=0.9,
    max_tokens=30
)

logging.debug(response)
print(response.choices[0].text)
