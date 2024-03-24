import pygame

from gameplay import *

# Initialize Pygame
pygame.init()

# Set up the screen
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
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)


def handle_checkpoint_screen(checkpoint_index):
    from list import start_game
    checkpoints_dict = [
        {"name": "First Day of Classes", "date": "08-27-2024"},
        {"name": "Midterm Exams", "date": "10-15-2024"},
        {"name": "Fall Break", "date": "11-20-2024"},
        {"name": "Finals", "date": "12-05-2024"},
        {"name": "Winter Break", "date": "12-10-2024"},
        {"name": "Spring Break", "date": "03-01-2025"},
        {"name": "Midterm Exams", "date": "03-25-2025"},
        {"name": "Summer!", "date": "05-10-2025"}
    ]
    checkpoint = checkpoints_dict[checkpoint_index]
    checkpoint_name = checkpoint["name"]
    screen.fill(WHITE)
    display_text("Checkpoint", BLACK, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    display_text(checkpoint_name, BLACK, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 30)
    display_text("Press Enter to observe, Spacebar to continue", BLACK, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 90)
    pygame.display.update()
    running = True
    while running:
        for evt in pygame.event.get():
            if evt.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evt.type == pygame.KEYDOWN:
                if evt.key == pygame.K_RETURN:
                    start_game()  # Exit the loop when user clicks on the popup
                    pygame.display.update()
                if evt.key == pygame.K_SPACE:
                    running = False
        # Clear the screen
        screen.fill(WHITE)
