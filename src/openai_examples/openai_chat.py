"""
This script is a simple example of how to use the OpenAI API to create a chatbot.
"""

from openai import OpenAI
from utilities import init
from openai_examples.openai_utilities import MODELS, message
import logging
logging.basicConfig(level=logging.INFO)

init()

def get_chat_completion(client: OpenAI) -> str | None:
    """
    Gets a chat completion from the OpenAI API.
    """
    try:
        completion = client.chat.completions.create(
            model=MODELS[0],
            messages=[
                message("system", "You are crazy advertisement guru."),
                message(
                    "user",
                    "Create three names that consist of two or more words for a brand selling fake alcohol!",
                ),
                message(
                    "assistant", "1. Faux Spirits\n2. Mocktail Makers\n3. Counterfeit Cocktails"
                ),
                message("user", "More sophisticated and a little french, please."),
            ],
        )
        return completion.choices[0].message.content
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def main():
    """
    Run the chat example.
    """
    client = OpenAI()
    completion = get_chat_completion(client)
    print(completion)

if __name__ == "__main__":
    main()
    