"""
A dialogue between two parties in a fictional world.
"""

import logging
from openai import OpenAI
from utilities import init
from openai_utilities import message, create_messages
from pydantic import BaseModel

class Language(BaseModel):
    question_to_go_on: str
    saidString: str

    def said(self, name, content):
        return f"{name} {self.saidString}: '{content}'"
    
english = Language(
    question_to_go_on="what is your answer?", 
    saidString="said")

german = Language(
    question_to_go_on="Was meinen Sie?", 
    saidString="sagt")

class Person(BaseModel):
    name: str
    prompt: str

    def description(self, world_description):
        return f"""
{self.prompt}

{world_description}
"""

class Dialogue:
    def __init__(self, world, persons, model, language):
        self.world = world
        self.persons = persons
        self.clients = { person.name: OpenAI() for person in persons}
        self.model = model
        self.language = language
        self.history = []

    def play(self, person, greeting, number_of_turns):
        print_message(self.language.said(person, greeting))
        self.add_to_history(person, greeting)
        for i in range(number_of_turns):
            for person in self.persons:
                self.turn(person.name, self.clients[person.name], person.description(self.world))

    def turn(self, name, client, system):
        messages = create_messages(
                                    message("system", system),
                                    self.history,
                                    message("user", f"{name} {self.language.question_to_go_on}")
                                )
        response = self.get_new_message(client, messages)
        print_message(response)
        self.add_to_history(name, response)

    def get_new_message(self, client, messages):
        "get the next message"
        response = client.chat.completions.create(
            model=self.model,
            messages=messages
        )
        logging.debug(response)
        message = response.choices[0].message.content
        return message

    def add_to_history(self, name, content):
        self.history.append(message("user", self.language.said(name, content)))

def print_message(content):
    print("---------------------------------------------------------------------")
    print(content)
    