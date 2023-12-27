"""
Utilities for the project.
"""
import os
import sys
import logging
import json
import yaml

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
    with open(path, 'w', encoding='utf-8') as outfile:
        json.dump(data, outfile)

def load_from_file(filename):
    if filename.endswith('.json'):
        content = _load_json(filename)
    elif filename.endswith('.yaml'):
        content = _load_yaml(filename)
    else:
        raise ValueError(f'Unknown file type: {filename}')
    return content

def _load_json(path):
    with open(path, 'r', encoding='utf-8') as file:
        content = file.read()
        return json.loads(content)

def _load_yaml(path):
    with open(path, 'r', encoding='utf-8') as yaml_file:
        content = yaml.safe_load(yaml_file)
        return content
