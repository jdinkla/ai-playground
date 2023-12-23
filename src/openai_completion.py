"""
Simple completion using OpenAI API
"""

import logging
from openai import OpenAI
from utilities import init

init()

MODEL = "gpt-3.5-turbo-instruct"

client = OpenAI()
response = client.completions.create(
    model=MODEL,
    prompt="Create a nice name for an AI consulting company that will lead us into a better future",
    temperature=0.2,
    max_tokens=30
)

logging.debug(response)
print(response.choices[0].text)
