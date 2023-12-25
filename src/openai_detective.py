"""
Simple completion using OpenAI API
"""

import argparse
import logging
from openai import OpenAI
from utilities import init
from openai_utilities import message

parser = argparse.ArgumentParser()
parser.add_argument("filename", help="the name of a file with a story")
args = parser.parse_args()

init()

PROMPT="""
You are an investigator and a detective.
The user will present you with a story of a crime and you will have to solve it. Explain your reasoning.
"""

with open(args.filename, 'r') as file:
    content = file.read()

MODEL = "gpt-3.5-turbo-1106"
#MODEL = "gpt-4-32k-0613"
#MODEL = "gpt-4-1106-preview"

client = OpenAI()
response = client.chat.completions.create(
    model=MODEL,
    messages=[
        message("system", PROMPT),
        message("user", content)
    ]
)
logging.debug(response)
print(response.choices[0].message.content)
