import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Game Over")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define font
font = pygame.font.Font(None, 36)


def game_over_screen():
    running = True
    clock = pygame.time.Clock()
    elapsed_time = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Close button clicked
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                running = False  # Exit the loop and return to gameplay screen


        # Clear the screen
        screen.fill(WHITE)

        # Display game over message
        game_over_text = font.render("Game Over", True, BLACK)
        game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(game_over_text, game_over_rect)

        # Display return to start screen message
        return_text = font.render("Click to return to start screen", True, BLACK)
        return_rect = return_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))
        screen.blit(return_text, return_rect)

        # Update the display
        pygame.display.update()

        elapsed_time += clock.tick_busy_loop(60)  # Limit frame rate to 60 FPS and get elapsed time

        # If elapsed time exceeds 3 seconds (3000 milliseconds), exit the loop
        if elapsed_time >= 3000:
            running = False


# Run the game over screen
if __name__ == "__main__":
    game_over_screen()
