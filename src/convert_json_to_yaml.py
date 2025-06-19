"""
Utility for converting the json examples to yaml.
"""
import argparse
import yaml

from domain import Scene

parser = argparse.ArgumentParser()
parser.add_argument("filename", help="the name of a json file")
args = parser.parse_args()

def convert_json_to_yaml(filename):
    "convert a json file to a yaml file"
    yaml_filename = filename.replace('.json', '.yaml')
    with open(filename, 'r', encoding='utf-8') as json_file:
        data = json_file.read()
    scene = Scene.model_validate_json(data)
    data = scene.model_dump()
    with open(yaml_filename, 'w', encoding='utf-8') as yaml_file:
        yaml.dump(data, yaml_file, allow_unicode=True)

convert_json_to_yaml(args.filename)
