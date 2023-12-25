"""
A dialogue between two parties in a fictional world.
"""

import logging
from utilities import init
from openai_dialogue import Dialogue, Person, Scene
from language import english

init(logging.WARNING)

#MODEL = "gpt-3.5-turbo-1106"
# MODEL = "gpt-4"
MODEL = "gpt-4-1106-preview"

with open('examples/dialogue.json', 'r') as file:
    content = file.read()
    scene = Scene.parse_raw(content)

dialogue = Dialogue(scene, MODEL, english)
dialogue.play(2)
