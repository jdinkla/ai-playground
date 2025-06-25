"""
This script uses the OpenAI API to convert text to speech.
"""
import argparse
from pathlib import Path
import openai as openai_lib
from utilities import init
from audio import play_mp3

def speak(client, message, voice):
    "Convert text to speech using OpenAI's TTS model and play the audio."
    response = client.audio.speech.create(
        model="tts-1",
        voice=voice,
        input=message
    )
    speech_file_path = Path(__file__).parent / ".." / "speech.mp3"
    response.stream_to_file(speech_file_path)
    play_mp3(speech_file_path)

def speak_subscriber(client, person, response):
    "Speak the response for a specific person."
    speak(client, response, person.voice)

init()

parser = argparse.ArgumentParser()
parser.add_argument("message", help="the message to speak")
args = parser.parse_args()

_client = openai_lib.OpenAI()
speak(_client, args.message, "nova")
