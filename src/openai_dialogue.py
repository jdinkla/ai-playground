"""
Dialog generator.
"""

import logging
from openai import OpenAI
from openai_utilities import MODELS, message, create_messages

class Dialogue:
    def __init__(self, scene, model=MODELS[0]):
        self.scene = scene
        self.model = model
        self.history = {person.name: [] for person in scene.persons}
        self.clients = {person.name: OpenAI() for person in scene.persons}
        self.prompts = {person.name: extended_prompt(scene.description, person.prompt) for person in scene.persons}
        self.subscribers = []

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)

    def play(self, number_of_turns):
        for i in range(number_of_turns):
            for person in self.scene.persons:
                self.turn(person)

    def turn(self, person):
        client = self.clients[person.name]
        chat_history = self.create_chat_history(person)
        response = get_response(self.model, client, chat_history)
        msg = create_message(person.name, response)
        self.add_to_histories(person.name, msg)
        for subscriber in self.subscribers:
            subscriber(client, person, response)

    def create_chat_history(self, person):
        name = person.name
        prompt = message("system", self.prompts[name])
        history = self.history[name]
        question = message("user", f"{name}?")
        return create_messages(prompt, history, question)

    def add_to_histories(self, name, msg):
        for key, value in self.history.items():
            value.append(message(get_role(key, name), msg))


def get_response(model, client, chat_history):
    response = client.chat.completions.create(
        model=model,
        messages=chat_history
    )
    logging.debug(response)
    return response.choices[0].message.content


def create_message(name, content):
    if name in content:
        msg = content
    else:
        msg = f"[{name}] {content}"
    return msg

def get_role(key, name):
    if key == name:
        role = "user"
    else:
        role = "assistant"
    return role

def extended_prompt(world_description, prompt):
    return f"""
{world_description}

{prompt}
"""

def stdout_subscriber(client, person, response):
    msg = create_message(person.name, response)
    print("----------------------------------------------------")
    print(msg)
    print()
