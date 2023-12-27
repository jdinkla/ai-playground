"""
Creates a dialogue from a json file.
"""

import argparse
import logging
from utilities import init
from openai_dialogue import Dialogue, Scene, stdout_subscriber

parser = argparse.ArgumentParser()
parser.add_argument("filename", help="the name of a json file", nargs="?", default="examples/dialogue.json")
parser.add_argument("turns", help="the number of turns", default=2, type=int)
args = parser.parse_args()

init(logging.WARNING)

MODEL = "gpt-3.5-turbo-1106"
#MODEL = "gpt-4"
#MODEL = "gpt-4-1106-preview"

with open(args.filename, 'r') as file:
    content = file.read()
    scene = Scene.parse_raw(content)

dialogue = Dialogue(scene, MODEL)
dialogue.subscribe(stdout_subscriber)
dialogue.play(args.turns)
