"""
This is an example of how to use the PromptTemplate.
"""
from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI
from langchain.chains import LLMChain
from utilities import init

init()

TEMPLATE = """
You describe an image for a text2image AI.
Describe the contents with keywords that can be recognised by the AI.
Use adjectives to describe details. 
Limit your answer to at most 75 words.
Do not use the following words: [knob].

Question: {question}
"""

prompt = PromptTemplate(
    input_variables=["question"],
    template=TEMPLATE
)

chain = LLMChain(llm=OpenAI(temperature=0.5), prompt=prompt)

response=chain.predict(question="Cookie monster finds a treasure chest")
print(response)
