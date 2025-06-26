"""
Utilities for OpenAI API
"""

import logging

# see https://platform.openai.com/docs/models/model-endpoint-compatibility
MODELS = ["gpt-4.1-nano-2025-04-14"]


def message(role, content):
    """Create a message dictionary for OpenAI chat API."""
    return {"role": role, "content": content}


def system_message(content):
    """Create a system message dictionary for OpenAI chat API."""
    return message("system", content)


def create_messages(prompt, history, question):
    """Create a list of messages for OpenAI chat API."""
    combined = history.copy()
    combined.insert(0, prompt)
    combined.append(question)
    return combined


def create_chat_history(person, prompt, history):
    """Create a chat history for OpenAI chat API."""
    prompt_as_message = message("system", prompt)
    question = message("user", f"{person.name}?")
    return create_messages(prompt_as_message, history, question)


def get_response(model, client, chat_history):
    """Get a response from the OpenAI chat API."""
    response = client.chat.completions.create(model=model, messages=chat_history)
    logging.debug(response)
    return response.choices[0].message.content


def create_message(name, content):
    """Create a message for OpenAI chat API."""
    if name in content:
        msg = content
    else:
        msg = f"[{name}] {content}"
    return msg


def get_role(key, name):
    """Get the role for a message."""
    if key == name:
        role = "user"
    else:
        role = "assistant"
    return role


def extended_prompt(world_description, prompt):
    """Create an extended prompt for OpenAI chat API."""
    return f"""
{world_description}

{prompt}
"""
