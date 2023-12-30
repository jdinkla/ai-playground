"""
Domain classes.
"""
from pydantic import BaseModel


class Person(BaseModel):
    name: str
    prompt: str
    voice: str = "nova"


class Scene(BaseModel):
    description: str
    persons: list[Person]
