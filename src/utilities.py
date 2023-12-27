"""
Utilities for the project.
"""
import os
import sys
import logging
import json

logggingFormat = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

def init(level = logging.DEBUG):
    "initialize the project"
    _check_env()
    logging.basicConfig(level=level, format=logggingFormat)

def _check_env():
    "check the environment variable OPENAI_API_KEY"
    if 'OPENAI_API_KEY' not in os.environ:
        print("OPENAI_API_KEY is not set. Exiting.")
        sys.exit(1)

def save_as_json(data, path):
    with open(path, 'w') as outfile:
        json.dump(data, outfile)
