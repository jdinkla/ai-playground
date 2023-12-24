"""
"""

from pathlib import Path
from utilities import play_mp3


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

def speak(client, message, voice):
    response = client.audio.speech.create(
        model="tts-1",
        voice=voice,
        input=message
    )
    speech_file_path = Path(__file__).parent / ".." / "speech.mp3"
    response.stream_to_file(speech_file_path)
    play_mp3(speech_file_path)
