"""
Classes for generating dialogues.
"""

import logging
from openai import OpenAI
from openai_utilities import message, create_messages,speak
from pydantic import BaseModel
from language import english

class Person(BaseModel):
    name: str
    prompt: str
    voice: str = "nova"

    def extended_prompt(self, world_description):
        return f"""
{world_description}

{self.prompt}
"""


class Dialogue:
    def __init__(self, world, persons, model = "gpt-3.5-turbo-1106", language = english, speak = False):
        self.world = world
        self.persons = persons
        self.model = model
        self.language = language
        self.speak = speak
        self.history = []
        self.clients = {person.name: OpenAI() for person in persons}
        self.prompts = {person.name: person.extended_prompt(self.world) for person in persons}

    def play(self, number_of_turns):
        for i in range(number_of_turns):
            for person in self.persons:
                client = self.clients[person.name]
                prompt = self.prompts[person.name]
                self.turn(person, client, prompt)

    def turn(self, person, client, initial_prompt):
        print("----------------------------------------------------")
        name = person.name
        messages = create_messages(message("system", initial_prompt),
                                   self.history,
                                   message("user", f"{name} {self.language.question_to_go_on}"))
        response = self.get_new_message(client, messages)
        self.add(name, response)
        if self.speak:
            speak(client, response, person.voice)
        
    def get_new_message(self, client, messages):
        "get the next message"
        response = client.chat.completions.create(
            model=self.model,
            messages=messages
        )
        logging.debug(response)
        message = response.choices[0].message.content
        return message

    def add(self, name, content):
        if name in content:
            msg = content
        else:
            msg = self.language.said(name, content)
        print(msg)
        self.history.append(message("user", msg))
        print() 