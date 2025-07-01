"""
Utilities for the project.
"""

import os
import sys
import logging
import json
import yaml
from pathlib import Path
import base64

LOGGING_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"


def init(level=logging.DEBUG):
    "initialize the project"
    _check_env()
    logging.basicConfig(level=level, format=LOGGING_FORMAT)


def _check_env():
    "check the environment variable OPENAI_API_KEY"
    if "OPENAI_API_KEY" not in os.environ:
        print("OPENAI_API_KEY is not set. Exiting.")
        sys.exit(1)


def save_as_json(data, path):
    "save data as JSON to a file"
    with open(path, "w", encoding="utf-8") as outfile:
        json.dump(data, outfile)


def load_from_file(filename):
    "load content from a file, either JSON or YAML"
    if filename.endswith(".json"):
        content = _load_json(filename)
    elif filename.endswith(".yaml"):
        content = _load_yaml(filename)
    else:
        raise ValueError(f"Unknown file type: {filename}")
    return content


def _load_json(path):
    with open(path, "r", encoding="utf-8") as file:
        content = file.read()
        return json.loads(content)


def _load_yaml(path):
    with open(path, "r", encoding="utf-8") as yaml_file:
        content = yaml.safe_load(yaml_file)
        return content


def rename_file(original_path: Path, new_name: str) -> Path:
    sanitized_name = new_name.replace(" ", "_").replace(":", "-")
    new_path = original_path.with_name(sanitized_name + original_path.suffix)

    counter = 1
    while new_path.exists():
        new_path = original_path.with_name(
            f"{sanitized_name}_{counter}{original_path.suffix}"
        )
        counter += 1

    original_path.rename(new_path)
    return new_path


def encode_image_to_base64(image_path):
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")
