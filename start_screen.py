import textwrap

import pygame
import sys

import main
from main import handle_option, BLACK, screen

start_game_menu = ["1. Study session", "2. Take a nap", "3. Exercise", "4. Shop/eat out", "5. Hang out with friends",
                   "6. Stop to party"]

def start_game():
    # Add code for starting the game or switching to the gameplay screen
    # while True:
    selected_option = 0
    running = True
    while running:
        # Handle events and update game state
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected_option = (selected_option - 1) % len(start_game_menu)
                elif event.key == pygame.K_DOWN:
                    selected_option = (selected_option + 1) % len(start_game_menu)
                elif event.key == pygame.K_RETURN:
                    handle_option(selected_option)
                elif pygame.K_1 <= event.key <= pygame.K_6:  # Check for number keys 1-6
                    num = event.key - pygame.K_1
                    handle_start_game(num)


        screen.fill(BLACK)

        # draw_text("Starting the game...", font, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4)
        main.draw_text("You may:", main.font, main.WHITE, main.SCREEN_WIDTH // 2, main.SCREEN_HEIGHT // 5)
        for i, option in enumerate(start_game_menu):
            color = main.GREEN if i == selected_option else main.WHITE
            main.draw_text(option, main.font, color, main.SCREEN_WIDTH // 2, 150 + i * 50)
        # print("Starting the game...")
        pygame.display.update()

def handle_start_game(start_index):
    selected_start_index = start_game_menu[start_index]
    if selected_start_index == "1. Study session":
        study_session()
    if selected_start_index == "2. Take a nap":
        nap()
    if selected_start_index == "3. Exercise":
        exercise()
    if selected_start_index == "4. Shop/eat out":
        shop()
    if selected_start_index == "5. Hang out with friends":
        hang_out()
    if selected_start_index == "6. Stop and party":
        party()




def study_session():
    print("study session!!")

def nap():
    print("nap zzzzzz")

def exercise():
    print("hoohahh exercise")

def shop():
    print("shop")

def hang_out():
    print("hang out")

def party():
    print("partayyyy")

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
                    main.options()

        screen.fill(BLACK)

        info_text = ("This game will show you the ups and downs of being a freshman... or first year... at UVA. "
                     "Proceed with caution...")
        # Split the long text into lines that fit the screen width
        info_lines = textwrap.wrap(info_text, width=60)

        # Display each line of the wrapped text
        y_offset = main.SCREEN_HEIGHT // 4  # Initial Y position for the text
        for line in info_lines:
            main.draw_text(line, main.font, main.WHITE, main.SCREEN_WIDTH // 2, y_offset)
            y_offset += 30  # Increase Y offset for the next line

        back_text = "Press 'b' to go back"
        back_color = main.GREEN if selected_option == len(main.options_list) else main.WHITE
        main.draw_text(back_text, main.font, back_color, main.SCREEN_WIDTH // 2, 150 + len(main.options_list) * 50)
        pygame.display.update()
