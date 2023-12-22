import os
import sys
import logging
import pygame

def init():
    _check_env()
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def _check_env():
    if 'OPENAI_API_KEY' not in os.environ:
        print("OPENAI_API_KEY is not set. Exiting.")
        sys.exit(1)

def play_mp3(path_to_mp3):
    pygame.mixer.init()
    pygame.mixer.music.load(path_to_mp3)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
