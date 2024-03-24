import textwrap

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
        start_game()
    elif selected_option_text == "2. Learn More":
        show_info()
    elif selected_option_text == "3. Turn Back":
        main_menu()
    elif selected_option_text == "4. Exit":
        pygame.quit()
        sys.exit()

def start_game():
    # Add code for starting the game or switching to the gameplay screen
    # while True:
    running = True
    while running:
        # Handle events and update game state
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(BLACK)

        draw_text("Starting the game...", font, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4)
        # print("Starting the game...")
        pygame.display.update()

def show_info():
    # Add code for showing information about the game or credits
    running = True
    selected_option = 0
    while running:
        # Handle events and update game state

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    options()

        screen.fill(BLACK)

        info_text = ("This game will show you the ups and downs of being a freshman... or first year... at UVA. "
                     "Proceed with caution...")
        # Split the long text into lines that fit the screen width
        info_lines = textwrap.wrap(info_text, width=60)

        # Display each line of the wrapped text
        y_offset = SCREEN_HEIGHT // 4  # Initial Y position for the text
        for line in info_lines:
            draw_text(line, font, WHITE, SCREEN_WIDTH // 2, y_offset)
            y_offset += 30  # Increase Y offset for the next line

        back_text = "Press 'b' to go back"
        back_color = GREEN if selected_option == len(options_list) else WHITE
        draw_text(back_text, font, back_color, SCREEN_WIDTH // 2, 150 + len(options_list) * 50)
        pygame.display.update()



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
