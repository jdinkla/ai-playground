"""
This script generates an image from a prompt using the OpenAI API.
"""
import argparse
import logging
from openai import OpenAI
from utilities import init

init()

parser = argparse.ArgumentParser()
parser.add_argument("prompt", help="the image prompt", default="Ernie and Bert eat cookies")
args = parser.parse_args()

client = OpenAI()
response = client.images.generate(
  model="dall-e-3",
  prompt=args.prompt,
  n=1,
  size="1024x1024",
)

logging.debug(response)

image_url = response.data[0].url
print(image_url)
