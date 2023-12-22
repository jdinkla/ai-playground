import os
import sys

def check_env():
    if 'OPENAI_API_KEY' not in os.environ:
        print("OPENAI_API_KEY is not set. Exiting.")
        sys.exit(1)
