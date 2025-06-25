"""
This is a sample script to demonstrate the use of the OpenAI LLM.
"""

from langchain_openai import OpenAI
from utilities import init

init()

llm = OpenAI()
response = llm("Tell me a joke about AI")
print(response)
