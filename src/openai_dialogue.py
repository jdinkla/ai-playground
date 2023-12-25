"""
Classes for generating dialogues.
"""

import logging
from openai import OpenAI
from openai_utilities import message, create_messages, speak
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


class Scene(BaseModel):
    description: str
    persons: list[Person]


class Dialogue:
    def __init__(self, scene, model="gpt-3.5-turbo-1106", language=english, speak=False):
        self.scene = scene
        self.world = scene.description
        self.persons = scene.persons
        self.model = model
        self.language = language
        self.speak = speak
        self.history = {person.name: [] for person in scene.persons}
        self.clients = {person.name: OpenAI() for person in scene.persons}
        self.prompts = {person.name: person.extended_prompt(
            self.world) for person in scene.persons}

    def play(self, number_of_turns):
        for i in range(number_of_turns):
            for person in self.persons:
                self.turn(person)

    def turn(self, person):
        print("----------------------------------------------------")
        client = self.clients[person.name]
        chat_history = self.create_history(person)
        response = self.get_response(client, chat_history)
        self.add(person.name, response)
        if self.speak:
            speak(client, response, person.voice)

    def create_history(self, person):
        name = person.name
        prompt = message("system", self.prompts[name])
        history = self.history[name]
        question = message("user", f"{name} {self.language.question_to_go_on}")
        return create_messages(prompt, history, question)

    def get_response(self, client, chat_history):
        "get the next message"
        response = client.chat.completions.create(
            model=self.model,
            messages=chat_history
        )
        logging.debug(response)
        message = response.choices[0].message.content
        return message

    def add(self, name, content):
        if name in content:
            msg = content
        else:
            msg = f"[{name}] {content}"
        print(msg)
        for key, value in self.history.items():
            if key == name:
                value.append(message("user", msg))
            else:
                value.append(message("assistant", msg))
        print()
