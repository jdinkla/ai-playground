"""
"""
from pydantic import BaseModel


class Language(BaseModel):
    question_to_go_on: str
    saidString: str

    def said(self, name, content):
        return f"[{name}] {content}"


english = Language(
    question_to_go_on="what is your answer?",
    saidString="said")

german = Language(
    question_to_go_on="Was meinen Sie?",
    saidString="sagt")
