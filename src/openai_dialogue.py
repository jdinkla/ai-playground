"""
Simple completion using OpenAI API
"""

import logging
from openai import OpenAI
from utilities import init
from openai_utilities import message

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

def get_new_message(client, messages):
    "get the next message"
    response = client.chat.completions.create(
        model=MODEL,
        messages=messages
    )
    logging.debug(response)
    message = response.choices[0].message.content        
    return message

def print_message(message):
    print("---------------------------------------------------------------------")
    print(message)
    print("---------------------------------------------------------------------")

messageA = get_new_message(clientA, [
        message("system", PROMPT_A),
        message("user", "Mr. A. start the discussion!"),
    ])
print_message(messageA)

messageB = get_new_message(clientB, [
        message("system", PROMPT_B),
        message("user", "Mr. A. said : '" + messageA + "'"),
        message("user", "Mrs. B. what is your answer?"),
    ])
print_message(messageB)

messageA = get_new_message(clientA, [
        message("system", PROMPT_A),
        message("user", "Mr. A. said : '" + messageA + "'"),
        message("user", "Mr. B. said : '" + messageB + "'"),
    ])
print_message(messageA)

# def create(prompt, messages, question):
#     combined = combine_messages(system_message(prompt), messages, question)
#     return combined
