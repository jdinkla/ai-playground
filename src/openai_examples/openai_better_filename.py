"""
This script uses the OpenAI API to look at an image and
finds a descriptive file name.
"""

import argparse

import openai as openai_lib
from openai_examples.openai_utilities import MODELS
from utilities import init, rename_file, encode_image_to_base64
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)

init()


def generate_filename(client, image_path):
    base64_image = encode_image_to_base64(image_path)
    response = client.chat.completions.create(
        model=MODELS[0],
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "You are an expert in naming files. Give a short (4–10 words) descriptive filename for this screenshot. Use snake case, do not use whitespace, but underscores '_' if needed.",
                    },
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/png;base64,{base64_image}"},
                    },
                ],
            }
        ],
    )
    return response.choices[0].message.content.strip()


def main():
    """
    Run the speech example.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="the image file")
    args = parser.parse_args()
    client = openai_lib.OpenAI()
    new_name = generate_filename(client, args.filename)
    renamed_name = rename_file(Path(args.filename), new_name)
    print(f"renamed to {renamed_name}")


if __name__ == "__main__":
    main()
