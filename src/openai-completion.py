from openai import Completion
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

response = Completion.create(
    model="text-davinci-003",
    prompt="Create a nice name for an AI consulting company that will lead us into a better future",
    temperature=0.2,
    max_tokens=30
)

logging.debug(response)
print(response["choices"][0]["text"])
