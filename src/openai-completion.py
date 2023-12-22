from openai import OpenAI
import logging
from utilities import init

init()

client = OpenAI()
response = client.completions.create(
    model="text-davinci-003",
    prompt="Create a nice name for an AI consulting company that will lead us into a better future",
    temperature=0.2,
    max_tokens=30
)

logging.debug(response)
logging.debug(response.choices)
print(response.model_dump_json(indent=2))
