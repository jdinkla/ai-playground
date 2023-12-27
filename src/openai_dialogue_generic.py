"""
Creates a dialogue from a json file.
"""

import argparse
import logging

from domain import Scene
from openai_utilities import MODELS
from utilities import init, load_from_file
from openai_dialogue import Dialogue, stdout_subscriber

parser = argparse.ArgumentParser()
parser.add_argument("filename", help="the name of a json file")
parser.add_argument("turns", help="the number of turns", default=2, type=int)
parser.add_argument("model", help="the OpenAI model", default=MODELS[0], choices=MODELS, nargs='?')
args = parser.parse_args()

init(logging.WARNING)

content = load_from_file(args.filename)
scene = Scene.model_validate(content)
    
dialogue = Dialogue(scene, args.model)
dialogue.subscribe(stdout_subscriber)
dialogue.play(args.turns)
