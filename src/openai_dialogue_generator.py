"""
Creates a dialogue from a short description in a json or yaml file.
"""

import argparse
import logging

from openai import OpenAI
from openai_utilities import MODELS, message
from utilities import init

parser = argparse.ArgumentParser()
parser.add_argument("description",
    help="the description of the scene of the dialogue including the peoples involved.")
parser.add_argument("model", help="the OpenAI model", default=MODELS[0], choices=MODELS, nargs='?')
args = parser.parse_args()

init(logging.WARNING)

PROMPT = """
You are a drama writer. 
The user will give a description of a scene of a dialogue or a discusssion and the people involved.
You will elaborate on the ideas of the user the create a nice description of the scene.
And you will instruct every person with a prompt (similiar to an LLM prompt like OpenAI) how they should behave and argue.
You will create a yaml file with the description of the scene and the prompts for every person. You use > for multi-line Strings. See the example below.

Example:

Input of the user: 
Modern Romeo and Juliet as Gangsta Rapper and Slacker.

Output in yaml:
---------------------------------------------
description: >
  This is the balcony scene similiar to 'Romeo and Juliet' by William Shakespeare but in 2023.
  Do not say more than 4 sentences.
persons:
- name: Romeo
  prompt: You are Romeo but more like a gangsta rapper, you speak short and precise. You want a date with Juliet.
  voice: onyx
- name: Juliet
  prompt: You are Julie but more like a Curt Cobain and you do not like to talk much.
  voice: nova
---------------------------------------------

The available voices are: alloy, echo, fable, onyx, nova, and shimmer
"""

client = OpenAI()
response = client.chat.completions.create(
    model=args.model,
    messages=[
        message("system", PROMPT),
        message("user", args.description)
    ]
)
logging.debug(response)
print(response.choices[0].message.content)
