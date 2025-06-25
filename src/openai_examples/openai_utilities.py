"""
Utilities for OpenAI API
"""

import logging

# see https://platform.openai.com/docs/models/model-endpoint-compatibility
MODELS = ["gpt-4.1-nano-2025-04-14"]

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


def create_chat_history(person, prompt, history):
    promptAsMessage = message("system", prompt)
    question = message("user", f"{person.name}?")
    return create_messages(promptAsMessage, history, question)


def get_response(model, client, chat_history):
    response = client.chat.completions.create(
        model=model,
        messages=chat_history
    )
    logging.debug(response)
    return response.choices[0].message.content


def create_message(name, content):
    if name in content:
        msg = content
    else:
        msg = f"[{name}] {content}"
    return msg


def get_role(key, name):
    if key == name:
        role = "user"
    else:
        role = "assistant"
    return role


def extended_prompt(world_description, prompt):
    return f"""
{world_description}

{prompt}
"""
