from langchain.llms import OpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain import PromptTemplate, OpenAI, LLMChain
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

template="""
You are AI and you are a strong supporter of functional programming in Haskell.
Try to win each argument with intelligent reasoning and cunning comparisons.

Current conversation:

{history}
Human: {input}
You:
"""

prompt = PromptTemplate(input_variables=['history', 'input'],    template=template)

llm = OpenAI(temperature=0.5)
memory = ConversationBufferMemory(return_messages=True)
conversation = ConversationChain(
    llm=llm, 
    verbose=True, 
    memory=memory,
    prompt=prompt
)

while True:
    user_input = input("Your question (or type 'exit' to quit): ")
    if user_input.lower() == "exit":
        break
    ai_response = conversation.predict(input=user_input)
    print(ai_response)
    memory.chat_memory.add_user_message(user_input)
    memory.chat_memory.add_ai_message(ai_response)
