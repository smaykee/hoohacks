import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants for colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Oregon Trail Game")

# Font settings
font = pygame.font.Font(None, 36)

def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_surface, text_rect)

def main_menu():
    while True:
        screen.fill(WHITE)
        draw_text("Oregon Trail Game", font, BLACK, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4)
        draw_text("Press Enter to Start", font, GREEN, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        draw_text("Press Esc to Quit", font, GREEN, SCREEN_WIDTH // 2, SCREEN_HEIGHT * 3 // 4)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    # Start the game or go to the main gameplay loop
                    return
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

if __name__ == "__main__":
    main_menu()
