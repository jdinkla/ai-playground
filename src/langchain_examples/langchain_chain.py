"""
Chain example using LangChain.
"""

import argparse
import logging
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from utilities import init

parser = argparse.ArgumentParser()
parser.add_argument(
    "topic", help="the topic of the joke", default="ice cream", nargs="?"
)
args = parser.parse_args()

init(logging.WARNING)

prompt = ChatPromptTemplate.from_template("tell me a short joke about {topic}")
model = ChatOpenAI()
output_parser = StrOutputParser()

chain = prompt | model | output_parser

response = chain.invoke({"topic": args.topic})
print(response)
