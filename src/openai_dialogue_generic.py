"""
Creates a dialogue from a json file.
"""

import argparse
import logging
from openai_utilities import MODELS
from utilities import init
from openai_dialogue import Dialogue, Scene, stdout_subscriber

parser = argparse.ArgumentParser()
parser.add_argument("filename", help="the name of a json file")
parser.add_argument("turns", help="the number of turns", default=2, type=int)
parser.add_argument("model", help="the OpenAI model", default=MODELS[0], choices=MODELS, nargs='?')
args = parser.parse_args()

init(logging.WARNING)

with open(args.filename, 'r') as file:
    content = file.read()
    scene = Scene.parse_raw(content)

dialogue = Dialogue(scene, args.model)
dialogue.subscribe(stdout_subscriber)
dialogue.play(args.turns)
