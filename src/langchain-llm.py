from langchain.llms import OpenAI
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

llm = OpenAI()
response = llm("Tell me a joke about AI")
print(response)
