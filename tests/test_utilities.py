import json
from domain import Person, Scene
from utilities import load_from_file, _load_json, _load_yaml


def test_load_json_should_return_content():
    data = _load_json("tests/examples/example.json")
    assert data["description"] == "This is the description"
    assert data["persons"].__len__() == 2
    assert data["persons"][0]["name"] == "A"
    assert data["persons"][0]["prompt"] == "You are A"
    assert data["persons"][0]["voice"] == "onyx"
    assert data["persons"][1]["name"] == "B"
    assert data["persons"][1]["prompt"] == "B is a person"
    assert data["persons"][1]["voice"] == "nova"


def test_load_yaml_should_return_content():
    content = _load_yaml("tests/examples/example.yaml")
    scene = Scene.model_validate(content)
    assert scene.description == "This is the description"
    assert scene.persons.__len__() == 2
    assert scene.persons[0] == Person(name="C", prompt="You are C", voice="onyx")
    assert scene.persons[1] == Person(
        name="D", prompt="D is a multi-line person\n", voice="nova"
    )


def test_load_from_file_should_return_content_if_json():
    content = load_from_file("tests/examples/example.json")
    scene = Scene.model_validate(content)
    assert scene.description == "This is the description"


def test_load_from_file_should_return_content_if_yaml():
    content = load_from_file("tests/examples/example.yaml")
    scene = Scene.model_validate(content)
    assert scene.description == "This is the description"
