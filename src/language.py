"""
"""
from pydantic import BaseModel


class Language(BaseModel):
    question_to_go_on: str


english = Language(
    question_to_go_on="what is your answer?",
)

german = Language(
    question_to_go_on="Was meinen Sie?",
)
