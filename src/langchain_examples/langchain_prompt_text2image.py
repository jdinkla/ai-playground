"""
This is an example of how to use the PromptTemplate.
"""

import argparse
from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI
from langchain.chains import LLMChain
from utilities import init

init()

TEMPLATE = """
You are an artist and generate a prompt for a text-to-image AI that translates the naive description into a detailed and creative image prompt.

Description: {description}
"""

prompt = PromptTemplate(input_variables=["description"], template=TEMPLATE)

chain = LLMChain(llm=OpenAI(temperature=0.5), prompt=prompt)

parser = argparse.ArgumentParser()
parser.add_argument("description", help="the description of the image")
args = parser.parse_args()

response = chain.predict(description=args.description)
print(response)
