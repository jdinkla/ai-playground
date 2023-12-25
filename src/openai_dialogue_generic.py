"""
A dialogue between two parties in a fictional world.
"""

import argparse
import logging
from utilities import init
from openai_dialogue import Dialogue, Person, Scene
from language import english

parser = argparse.ArgumentParser()
parser.add_argument("filename", help="the name of a json file", nargs="?", default="examples/dialogue.json")
args = parser.parse_args()


init(logging.WARNING)

MODEL = "gpt-3.5-turbo-1106"
#MODEL = "gpt-4"
#MODEL = "gpt-4-1106-preview"

with open(args.filename, 'r') as file:
    content = file.read()
    scene = Scene.parse_raw(content)

dialogue = Dialogue(scene, MODEL, english)
dialogue.play(2)
