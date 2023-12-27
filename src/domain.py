from pydantic import BaseModel
import yaml


class Person(BaseModel):
    name: str
    prompt: str
    voice: str = "nova"


class Scene(BaseModel):
    description: str
    persons: list[Person]

