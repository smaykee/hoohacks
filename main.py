import textwrap

import pygame
import sys

#from options import *
import list
from gameplay import *

# Initialize Pygame
pygame.init()

# Constants for colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Wahoo Trails")

# Font settings
font = pygame.font.Font(None, 36)

# Initialize the mixer for sound
pygame.mixer.init()
# Load sound files
button_click_sound = pygame.mixer.Sound("Walking Towards A Stream.wav")

options_list = ["1. Begin Your Journey...", "2. Learn More", "3. Turn Back", "4. Exit"]


def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_surface, text_rect)


def main_menu():
    while True:
        screen.fill(BLACK)
        draw_text("First Year Fumbles", font, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4)
        draw_text("Press Enter to Start", font, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        draw_text("Press Esc to Quit", font, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT * 3 // 4)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    # Play button click sound
                    button_click_sound.play()
                    # Go to the options screen
                    return "options"
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()


def options():
    running = True
    selected_option = 0
    while running:
        screen.fill(BLACK)  # Change background color or draw gameplay elements
        draw_text("Options", font, WHITE, SCREEN_WIDTH // 2, 50)
        for i, option in enumerate(options_list):
            color = GREEN if i == selected_option else WHITE
            draw_text(option, font, color, SCREEN_WIDTH // 2, 150 + i * 50)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected_option = (selected_option - 1) % len(options_list)
                elif event.key == pygame.K_DOWN:
                    selected_option = (selected_option + 1) % len(options_list)
                elif event.key == pygame.K_RETURN:
                    handle_option(selected_option)
                elif pygame.K_1 <= event.key <= pygame.K_4:  # Check for number keys 1-4
                    num = event.key - pygame.K_1
                    handle_option(num)


def handle_option(option_index):
    selected_option_text = options_list[option_index]
    if selected_option_text == "1. Begin Your Journey...":
        gameplay_screen()
    elif selected_option_text == "2. Learn More":
        list.show_info()
    elif selected_option_text == "3. Turn Back":
        main_menu()
    elif selected_option_text == "4. Exit":
        pygame.quit()
        sys.exit()


def main():
    current_state = "menu"
    while True:
        if current_state == "menu":
            next_state = main_menu()
            if next_state == "options":
                current_state = "options"
                pygame.mixer.stop()  # Stop main menu music if playing
        elif current_state == "options":
            options()


if __name__ == "__main__":
    main()
