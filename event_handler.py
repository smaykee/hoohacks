import random

import pygame
import sys
import json


pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Event Pop-up")

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


def handle_event(event_data, gpa, mental_health, physical_health):
    running = True
    while running:
        for evt in pygame.event.get():
            if evt.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evt.type == pygame.KEYDOWN:
                if evt.key == pygame.K_RETURN:
                    running = False  # Exit the loop when user clicks on the popup

        # Clear the screen
        screen.fill(WHITE)

        # Display event message
        display_text("Event Pop-up", BLACK, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        display_text(event_data["name"], BLACK, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 30)
        display_text(event_data["desc"], BLACK, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 60)
        display_text("Press Enter to continue", BLACK, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 90)

        # Update the display
        pygame.display.update()

    # Process event after user clicks on the popup
    if event_data["name"] == "Honor code violation":
        gpa -= 0.5  # Drop GPA by 0.5
    elif event_data["name"] == "Fight with friends":
        mental_health -= random.randint(5, 20)  # Drop mental health by random integer between 5-20
    elif event_data["name"] == "Contracted an illness":
        physical_health -= random.randint(10, 30)  # Drop physical health by random integer between 10-30

    # Ensure stats are within bounds (0-100 for mental and physical health)
    gpa = max(gpa, 0)  # Ensure GPA doesn't go below 0
    mental_health = max(mental_health, 0)  # Ensure mental health doesn't go below 0
    physical_health = max(physical_health, 0)  # Ensure physical health doesn't go below 0

    # Write updated stats to file
    write_to_file({"gpa": gpa, "mental_health": mental_health, "physical_health": physical_health})


def handle_list_event(list_event_name, num):
    if list_event_name == "1. Pull an all-nighter":
        modify_file("physical_health", -10)
        modify_file("gpa", 0.05)
    elif list_event_name == "2. Take a nap":
        modify_file("physical_health", num)
    elif list_event_name == "3. Exercise":
        modify_file("physical_health", num)
    elif list_event_name == "4. Shop/eat out":
        modify_file("mental_health", num)
    elif list_event_name == ["5. Hang out with friends"]:
        modify_file("mental_health", num)
    elif list_event_name == ["6. Stop to party"]:
        modify_file("mental_health", num)
