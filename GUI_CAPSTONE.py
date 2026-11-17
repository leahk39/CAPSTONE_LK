import pygame
import math
import random
from pygame import mixer
import os

# initialize pygame
pygame.init()
mixer.init()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# create the screen
screen = pygame.display.set_mode((800, 600))

# title and icon
pygame.display.set_caption("Cats Life")
icon = pygame.image.load(os.path.join(BASE_DIR, 'cat.png'))
pygame.display.set_icon(icon)

# test to see if the code is running
print("GUI_CAPSTONE.py is running")

# game loop
running = True
while running:

    # RGB - red, green, blue
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False