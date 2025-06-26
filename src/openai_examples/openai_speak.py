"""
This script uses the OpenAI API to convert text to speech.
"""

import argparse
from pathlib import Path
import openai as openai_lib
from utilities import init
from audio import play_mp3
import logging

logging.basicConfig(level=logging.INFO)


init()

speech_file_path = Path(__file__).parent / ".." / "speech.mp3"


def speak(client, message, voice):
    "Convert text to speech using OpenAI's TTS model and play the audio."
    with client.audio.speech.with_streaming_response.create(
        model="tts-1", voice=voice, input=message
    ) as response:
        response.stream_to_file(speech_file_path)
    play_mp3(speech_file_path)


def main():
    """
    Run the speech example.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("message", help="the message to speak")
    parser.add_argument(
        "voice",
        nargs="?",
        help="the voice to use",
        default="nova",
        choices=[
            "alloy",
            "ash",
            "ballad",
            "coral",
            "echo",
            "fable",
            "nova",
            "onyx",
            "sage",
            "shimmer",
        ],
    )
    args = parser.parse_args()

    client = openai_lib.OpenAI()
    speak(client, args.message, args.voice)


if __name__ == "__main__":
    main()
