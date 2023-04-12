from langchain import PromptTemplate, OpenAI, LLMChain

template = """
You describe an image for a text2image AI.
It Is important to describe the contents with keywords that can be recognised by the AI.
Use adjectives to describe details. 
Limit your answer to at most 75 words.
Do not use the following words: [knob].

Question: {question}
"""

prompt = PromptTemplate(
    input_variables=["question"],
    template=template
)

chain = LLMChain(llm=OpenAI(temperature=0.5), prompt=prompt)

question="Cookie monster finds a treasure chest"

print(chain.predict(question=question))


