"""
"""

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
