"""
Domain classes.
"""
from pydantic import BaseModel


class Person(BaseModel):
    "A person in the scene, with a name, prompt, and voice."
    name: str
    prompt: str
    voice: str = "nova"

class Scene(BaseModel):
    "A scene in the dialogue, with a description, and a list of persons."
    description: str
    persons: list[Person]
