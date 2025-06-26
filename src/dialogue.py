"""
Dialog generator.
"""

from openai_examples.openai_utilities import (
    create_chat_history,
    create_message,
    extended_prompt,
    get_response,
    get_role,
    message,
)


class Dialogue:
    """Handles dialogue logic between clients."""

    def __init__(self, scene, client_factory):
        """Initialize Dialogue with a client factory."""
        self.scene = scene
        self.history = {person.name: [] for person in scene.persons}
        self.clients = {person.name: client_factory() for person in scene.persons}
        self.prompts = {
            person.name: extended_prompt(scene.description, person.prompt)
            for person in scene.persons
        }
        self.subscribers = []

    def subscribe(self, subscriber):
        """Subscribe to the dialogue."""
        self.subscribers.append(subscriber)

    def play(self, number_of_turns, model):
        """Play the dialogue."""
        for _ in range(number_of_turns):
            for person in self.scene.persons:
                self.turn(person, model)

    def turn(self, person, model):
        """Play a turn."""
        name = person.name
        client = self.clients[name]
        chat_history = create_chat_history(
            person, self.prompts[name], self.history[name]
        )
        response = get_response(model, client, chat_history)
        msg = create_message(name, response)
        self.add_to_histories(name, msg)
        for subscriber in self.subscribers:
            subscriber(client, person, response)

    def add_to_histories(self, name, msg):
        """Add a message to the history."""
        for key, value in self.history.items():
            value.append(message(get_role(key, name), msg))


def stdout_subscriber(_, person, response):
    """Print the response to the console."""
    msg = create_message(person.name, response)
    print("----------------------------------------------------")
    print(msg)
    print()
