from pydantic import BaseModel


class Person(BaseModel):
    name: str
    prompt: str
    voice: str = "nova"


class Scene(BaseModel):
    description: str
    persons: list[Person]


def load_from_json(path):
    with open(path, 'r') as file:
        content = file.read()
        scene = Scene.parse_raw(content)
    return scene
