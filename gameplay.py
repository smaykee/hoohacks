import pygame
import sys
import random
import json
from datetime import datetime, timedelta
from checkpoint_handler import *
from event_handler import *
from gameover import *
from main import *
from list import *

# Initialize Pygame
pygame.init()

# Set up the screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define font
font = pygame.font.Font(None, 24)

# Main checkpoints data
checkpoints = [
    {"name": "First Day of Classes", "date": "08-27-2024"},
    {"name": "Midterm Exams", "date": "10-15-2024"},
    {"name": "Fall Break", "date": "11-20-2024"},
    {"name": "Finals", "date": "12-05-2024"},
    {"name": "Winter Break", "date": "12-10-2024"},
    {"name": "Spring Break", "date": "03-01-2025"},
    {"name": "Midterm Exams", "date": "03-25-2025"},
    {"name": "Summer!", "date": "05-10-2025"}
]
events = [
    {"name": "Honor code violation", "desc": "The honor council finds you guilty. Your GPA has dropped."},
    {"name": "Fight with friends", "desc": "Caught up in drama. Your mental health has dropped."},
    {"name": "Contracted an illness", "desc": "Frat flu? COVID? Your physical health has dropped."}
]

# Player beginning stats
mental_health = 100
physical_health = 100
gpa = 4.0

date = "08-28-2024"  # starting date


def increment_date(curr_date, increment):
    global days_passed
    curr_date_obj = datetime.strptime(curr_date, "%m-%d-%Y")
    next_date_obj = curr_date_obj + timedelta(days=increment)
    next_date_str = next_date_obj.strftime("%m-%d-%Y")
    days_passed += increment

    return next_date_str


def read_from_file():
    with open("stats.txt", "r") as file:
        data = json.load(file)
    global gpa
    global mental_health
    global physical_health

    with open("stats.txt", "r") as file:
        data = json.load(file)

    gpa = data.get("gpa", gpa)
    mental_health = data.get("mental_health", mental_health)
    physical_health = data.get("physical_health", physical_health)


def display_text(text, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    screen.blit(text_surface, text_rect)

    # Update player stats based on game events, actions, etc.


def check_stats():
    if gpa == 0 or mental_health == 0 or physical_health == 0:
        game_over_screen()

def gameplay_screen():
    global mental_health, physical_health, gpa, date, days_passed, event
    start_date = datetime.strptime("08-27-2024", "%m-%d-%Y")

    checkpoint_index = 1
    event_popup_active = False
    # Main loop
    running = True
    while running:
        # Handle events from user
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # close button
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    list.start_game()  # Exit the loop when user clicks on the popup
                    pygame.display.update()

        # Clear the screen
        screen.fill(WHITE)
        curr_date = datetime.strptime(date, "%m-%d-%Y")
        days_passed = (curr_date - start_date).days
        # Display date, days passed, time until next landmark
        display_text(f"Date: {date}", BLACK, 20, 20)
        display_text(f"Days Passed: {days_passed}", BLACK, 20, 50)

        # Display player stats
        display_text(f"Mental Health: {mental_health}", BLACK, 20, 120)
        display_text(f"Physical Health: {physical_health}", BLACK, 20, 150)
        display_text(f"GPA: {gpa}", BLACK, 20, 180)

        # Main loop for game
        while checkpoint_index < len(checkpoints):
            if curr_date.date() == datetime.strptime(checkpoints[checkpoint_index]["date"], "%m-%d-%Y").date():
                # Call handle_checkpoint_screen with the checkpoint data
                handle_checkpoint_screen(checkpoint_index)
                checkpoint_index += 1
                break
            else:
                check_stats()
                # If no checkpoint is reached, increment the date and days passed
                if not event_popup_active:
                    days_passed += 1
                    date = increment_date(date, 1)

                # Update the display
                pygame.display.update()

                # Add a delay to control the game's speed
                pygame.time.delay(100)  # Adjust the delay as needed

                # Random events
                if random.random() < 0.05:
                    event_index = random.randint(0, len(events) - 1)
                    event = events[event_index]
                    handle_event(event, gpa, mental_health, physical_health)
                    read_from_file()
                    event_popup_active = True


                else:
                    event_popup_active = False
                break
        # Display moving animation
        # Implement moving background or sprites here
        # Update the display
        pygame.display.update()



