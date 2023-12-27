"""
"""

from pathlib import Path

MODELS = ["gpt-3.5-turbo-1106", "gpt-4-32k-0613", "gpt-4-1106-preview"]

def message(role, content):
    return {
        "role": role,
        "content": content
    }

def system_message(content):
    return message("system", content)

def create_messages(prompt, history, question):
    combined = history.copy()
    combined.insert(0, prompt)
    combined.append(question)
    return combined
