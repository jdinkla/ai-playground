"""
Utilities for sound.
"""
import pygame

def play_mp3(path_to_mp3):
    "play an mp3 file"
    pygame.mixer.init()
    pygame.mixer.music.load(path_to_mp3)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
