"""
Utilities for the project.
"""
import os
import sys
import logging
import pygame

def init():
    "initialize the project"
    _check_env()
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def _check_env():
    "check the environment variable OPENAI_API_KEY"
    if 'OPENAI_API_KEY' not in os.environ:
        print("OPENAI_API_KEY is not set. Exiting.")
        sys.exit(1)

def play_mp3(path_to_mp3):
    "play an mp3 file"
    pygame.mixer.init()
    pygame.mixer.music.load(path_to_mp3)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
