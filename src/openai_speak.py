"""
This script uses the OpenAI API to convert text to speech.
"""
import argparse
from pathlib import Path
from openai import OpenAI
from utilities import init
from audio import play_mp3

def speak(client, message, voice):
    response = client.audio.speech.create(
        model="tts-1",
        voice=voice,
        input=message
    )
    speech_file_path = Path(__file__).parent / ".." / "speech.mp3"
    response.stream_to_file(speech_file_path)
    play_mp3(speech_file_path)

def speak_subscriber(client, person, response):
    speak(client, response, person.voice)

init()

parser = argparse.ArgumentParser()
parser.add_argument("message", help="the message to speak")
args = parser.parse_args()

client = OpenAI()
speak(client, args.message, "nova")
