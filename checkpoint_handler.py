import random

import pygame
import sys
import json
import main
from gameplay import *

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Checkpoint Pop-up")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define font
font = pygame.font.Font(None, 24)

def write_to_file(data):
    with open("stats.txt", "w") as file:
        json.dump(data, file)


def modify_file(stat_name, num):
    with open("stats.txt", "r") as file:
        data = json.load(file)

    data[stat_name] += num

    with open("stats.txt", "w") as file:
        json.dump(data, file)

def display_text(text, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_surface, text_rect)

def handle_checkpoint(checkpoint_index):
    if checkpoint_index == 0:handle_checkpoint0()
    if checkpoint_index == 1: handle_checkpoint1()
    if checkpoint_index == 2: handle_checkpoint2()
    if checkpoint_index == 3: handle_checkpoint3()
    if checkpoint_index == 4: handle_checkpoint4()
    if checkpoint_index == 5: handle_checkpoint5()
    if checkpoint_index == 6: handle_checkpoint6()
    if checkpoint_index == 7: handle_checkpoint7()

def handle_checkpoint0():
    display_text(checkpoints[0]["name"], BLACK, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 30)
def handle_checkpoint1():
    display_text(checkpoints[1]["name"], BLACK, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 30)

def handle_checkpoint2():
    display_text(checkpoints[2]["name"], BLACK, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 30)

def handle_checkpoint3():
    display_text(checkpoints[3]["name"], BLACK, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 30)
def handle_checkpoint4():
    display_text(checkpoints[4]["name"], BLACK, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 30)

def handle_checkpoint5():
    display_text(checkpoints[5]["name"], BLACK, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 30)

def handle_checkpoint6():
    display_text(checkpoints[6]["name"], BLACK, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 30)

def handle_checkpoint7():
    display_text(checkpoints[7]["name"], BLACK, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 30)
