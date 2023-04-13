from openai import Image
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

response = Image.create(
  prompt="Ernie and Bert eat cookies",
  n=1,
  size="256x256"
)
logging.debug(response)
image_url = response['data'][0]['url']
print(image_url)
