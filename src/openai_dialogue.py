"""
A dialogue between two parties in a fictional world.
"""

import logging
from openai import OpenAI
from utilities import init
from openai_utilities import message, create_messages

init()

NAME_M = "Mrs. M."
NAME_A = "Mr. Arenheit"
NAME_B = "Mrs. Berkel"

WORLD_DESCRIPTION = f"""
This dialogue is part of a TV discussion in a fictional world. 

Since 5 years the economy is in misarray because of the high inflation. 
The people are increasingly unhappy and looking for alternatives.
Almost all citizens are watching the discussion, so it is very important to win the discussion.

The A party believes similiar to the novel "Fahrenheit 451" that books are dangerous and should be banned. 
The book itself is not known in this fictional world.
The leader of the A party is {NAME_A}.
The A party is part of the opposition. 
The other parties are very small. 

The B party is ruling the country.
The B party believes in free speech similiar as Germany today. 
{NAME_B} is leader of the B party and is ruling the country. 

People involved in the discussion:
    - {NAME_M} is the moderator of the discussion. 
    - {NAME_B}
    - {NAME_A}
"""


PROMPT_A = f"""
You are taking part in an TV discussion in a fictional world. Your name is {NAME_A} and you are a politician and leader of the A party. 
You really think that books are dangerous and should be banned. 
It is your personal mission.
If someone uses a quote, you try to use another quote from the same person that prooves your point and not theirs.
If you answer to a statement of {NAME_B}, pick a weak argument and try to win the viewers over to your side.
Maybe this is your last chance to win the election - ever.
"""

PROMPT_B = f"""
You are taking part in an TV discussion in a fictional world. 
Your name is {NAME_B} and you are a politician and leader of the B party.
You see freedom of speech and books as necessary for a economic succesful society. 
The opposition is clearly clueless but you fear that people may believe them because you have not invested enough in education.
You like to quote famous people and books. But because many people have no higher education, you prefer simple quotes.
"""

SYSTEM_A = f"""
{PROMPT_A}

{WORLD_DESCRIPTION}
"""

SYSTEM_B = f"""
{PROMPT_B}

{WORLD_DESCRIPTION}
"""


# MODEL = "gpt-3.5-turbo-1106"
MODEL = "gpt-4"
# MODEL = "gpt-4-1106-preview"

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


def print_message(content):
    print("---------------------------------------------------------------------")
    print(content)
    print("---------------------------------------------------------------------")

def said(name, message):
    return f"{name} said: '{message}'"

history = []

def add_to_history(content):
    history.append(message("user", content))

add_to_history(said(NAME_M, 'Welcome to the discussion! We are talking about the next election. What is your party going to do?'))


messageA = get_new_message(clientA,
                           create_messages(
                               message("system", SYSTEM_A),
                               history,
                               message("user", f"{NAME_A} start the discussion!")
                           )
                           )
print_message(messageA)
add_to_history(said(NAME_A, messageA))

messageB = get_new_message(clientB, 
                           create_messages(
                               message("system", SYSTEM_B),
                               history,
                               message("user", f"{NAME_B} what is your answer?")
                           )
                           )
print_message(messageB)
add_to_history(said(NAME_B, messageB))

messageA = get_new_message(clientA, 
                           create_messages(
                                 message("system", SYSTEM_A),
                                 history,
                                 message("user", f"{NAME_A} what is your answer?")
                            )
                            )
print_message(messageA)
add_to_history(said(NAME_A, messageA))

print(history)
