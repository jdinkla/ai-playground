"""
Simple completion using OpenAI API
"""

import logging
from openai import OpenAI
from utilities import init

init()

PROMPT_A="""
You are taking part in an TV discussion (in a fictional world). 
Your name is Mr. A and you are a politician and leader of the A party. Your party is part of the opposition. 

The A party believes similiar to the novel "Fahrenheit 451" that books are dangerous and should be banned.

The other people in the discussion are Mrs. Berkel and Mrs. M the moderator.

Mrs. Berkel is leader of the B party and is ruling the country. 
The B party believes in free speech similiar as Germany today. Since 5 years the economy is in misarray because of the high inflation. 
And the people are unhappy and looking for alternatives.

If you answer to a statement of Mrs. Berkel, pick a weak argument and try to win the viewers over to your side.
"""

PROMPT_B="""
You are taking part in an TV discussion (in a fictional world).

Your name is Mrs. Berkel and you are a politician and leader of the B party. Your party is ruling the country. 
Your party is believes in free speech similiar as Germany today. Since 5 years the economy is in misarray because of the high inflation. 
And the people are unhappy and looking for alternatives.

The other people in the discussion are Mrs. A from the A Party and Mrs. M the moderator.

The A party believes similiar to the novel "Fahrenheit 451" that books are dangerous and should be banned.
"""


#MODEL = "gpt-3.5-turbo-1106"
MODEL = "gpt-4"
#MODEL = "gpt-4-1106-preview"

clientA = OpenAI()
clientB = OpenAI()

responseA = clientA.chat.completions.create(
    model=MODEL,
    messages=[
        {
            "role": "system",
            "content": PROMPT_A
        },
        {
            "role": "user",
            "content": "Mr. A. start the discussion!"
        }
    ]
)

logging.debug(responseA)
messageA = responseA.choices[0].message.content
print("---------------------------------------------------------------------")
print(messageA)
print("---------------------------------------------------------------------")


responseB = clientB.chat.completions.create(
    model=MODEL,
    messages=[
        {
            "role": "system",
            "content": PROMPT_B
        },
        {
            "role": "user",
            "content": "Mr. A. said : '" + messageA + "'"
        },
        {
            "role": "user",
            "content": "Mrs. B. what is your answer?"
        },
    ]
)

logging.debug(responseB)
messageB = responseB.choices[0].message.content
print("---------------------------------------------------------------------")
print(messageB)
print("---------------------------------------------------------------------")

responseA = clientA.chat.completions.create(
    model=MODEL,
    messages=[
        {
            "role": "system",
            "content": PROMPT_A
        },
         {
            "role": "user",
            "content": "Mr. A. said : '" + messageA + "'"
        },
        {
            "role": "user",
            "content": "Mrs. B. said : '" + messageB + "'"
        },
        {
            "role": "user",
            "content": "Mr. A. what is your answer?"
        },
    ]
)

logging.debug(responseA)
messageA = responseA.choices[0].message.content
print("---------------------------------------------------------------------")
print(messageA)
print("---------------------------------------------------------------------")

