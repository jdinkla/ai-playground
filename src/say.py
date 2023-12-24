"""
This script uses the OpenAI API to convert text to speech.
"""
import argparse
from pathlib import Path
from openai import OpenAI
from utilities import init, play_mp3

init()

parser = argparse.ArgumentParser()
parser.add_argument("message", help="the message to speak",
                    default="Ernie and Bert eat cookies")
args = parser.parse_args()

client = OpenAI()

speech_file_path = Path(__file__).parent / ".." / "speech.mp3"
response = client.audio.speech.create(
    model="tts-1",
    voice="nova",
    input=args.message
)

response.stream_to_file(speech_file_path)
play_mp3(speech_file_path)
