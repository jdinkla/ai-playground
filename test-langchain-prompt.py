from langchain import PromptTemplate, OpenAI, LLMChain

template = """
You are Marvin, the robot from the Hitchhiker's Guide working as a consultant giving an answer to a question.

When you are asked, you give the correct answer. If you do not know or are unsure, say so. 
Always ensure that the client understands that you are clearly overqualified for this task. Say so explicitly.

Question: {question}
"""

prompt = PromptTemplate(
    input_variables=["question"],
    template=template
)

chain = LLMChain(llm=OpenAI(temperature=0.5), prompt=prompt)

question="Where does moonlight come from?"

print(chain.predict(question=question))


