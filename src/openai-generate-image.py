from openai import OpenAI
from check_env import check_env
import argparse
import logging

check_env()

parser = argparse.ArgumentParser()
parser.add_argument("prompt", help="the image prompt", default="Ernie and Bert eat cookies")
args = parser.parse_args()

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

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
