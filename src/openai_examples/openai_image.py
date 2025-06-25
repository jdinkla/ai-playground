"""
This script generates an image from a prompt using the OpenAI API.
"""

import argparse
import logging
import openai as openai_lib
from utilities import init

init()

parser = argparse.ArgumentParser()
parser.add_argument("prompt", help="the prompt that describes the image")
args = parser.parse_args()

client = openai_lib.OpenAI()
response = client.images.generate(
    model="dall-e-3",
    prompt=args.prompt,
    n=1,
    size="1024x1024",
)

logging.debug(response)

image_url = response.data[0].url
print("Click on the following URL to view the image:")
print(image_url)
