import textwrap
import time
import pygame
import sys
import random

import gameplay
import main
from checkpoint_handler import BLACK, WHITE, SCREEN_WIDTH, SCREEN_HEIGHT
from main import screen
from event_handler import handle_list_event

start_game_menu = ["1. Pull an all-nighter", "2. Take a nap", "3. Exercise", "4. Shop/eat out",
                   "5. Hang out with friends",
                   "6. Stop to party"]


def start_game():
    # Add code for starting the game or switching to the gameplay screen
    # while True:
    selected_option = 0
    running = True
    while running:
        # Handle events and update game state...
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
                    main.handle_option(selected_option)
                elif pygame.K_1 <= event.key <= pygame.K_6:  # Check for number keys 1-6
                    num = event.key - pygame.K_1
                    handle_start_game(num)
                elif event.key == pygame.K_q:  # Quit button
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_b:  # Go back button...
                    gameplay.gameplay_screen()

        screen.fill(BLACK)

        # draw_text("Starting the game...", font, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4)
        main.draw_text("You may:", main.font, main.WHITE, main.SCREEN_WIDTH // 2, main.SCREEN_HEIGHT // 5)
        for i, option in enumerate(start_game_menu):
            color = main.GREEN if i == selected_option else main.WHITE
            main.draw_text(option, main.font, color, main.SCREEN_WIDTH // 2, 150 + i * 50)

        main.draw_text("Quit (Press 'q')", main.font, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT - 60)
        main.draw_text("Go back (Press 'b')", main.font, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT - 30)
        # print("Starting the game...")
        pygame.display.update()


def handle_start_game(start_index):
    selected_start_index = start_game_menu[start_index]
    if selected_start_index == "1. Pull an all-nighter":
        all_nighter()
        handle_list_event(selected_start_index, -1)
    if selected_start_index == "2. Take a nap":
        nap()
        handle_list_event(selected_start_index, 2)
    if selected_start_index == "3. Exercise":
        exercise()
        handle_list_event(selected_start_index, 3)
    if selected_start_index == "4. Shop/eat out":
        shop()
        handle_list_event(selected_start_index, 5)
    if selected_start_index == "5. Hang out with friends":
        if hang_out():
            handle_list_event(selected_start_index, 10)
        else:
            handle_list_event(selected_start_index, 0)
    if selected_start_index == "6. Stop to party":
        if not party():
            handle_list_event(selected_start_index, -20)
        else:
            handle_list_event(selected_start_index, 15)


def all_nighter():
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
                    start_game()

        screen.fill(BLACK)

        info_text = ("Your grades may increase but your health will suffer...spend your time wisely")
        # Split the long text into lines that fit the screen width
        info_lines = textwrap.wrap(info_text, width=60)

        # Display each line of the wrapped text
        y_offset = main.SCREEN_HEIGHT // 4  # Initial Y position for the text
        for line in info_lines:
            main.draw_text(line, main.font, main.WHITE, main.SCREEN_WIDTH // 2, y_offset)
            y_offset += 30  # Increase Y offset for the next line

        back_text = "Press 'b' to go back"
        back_color = main.GREEN if selected_option == len(start_game_menu) else main.WHITE
        main.draw_text(back_text, main.font, back_color, main.SCREEN_WIDTH // 2, 150 + len(main.options_list) * 50)
        pygame.display.update()


def nap():
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
                    start_game()

        screen.fill(BLACK)

        info_text = ("zzzzzzz...feeling refreshed! Sure hope my GPA and social life don't suffer!")
        # Split the long text into lines that fit the screen width
        info_lines = textwrap.wrap(info_text, width=60)

        # Display each line of the wrapped text
        y_offset = main.SCREEN_HEIGHT // 4  # Initial Y position for the text
        for line in info_lines:
            main.draw_text(line, main.font, main.WHITE, main.SCREEN_WIDTH // 2, y_offset)
            y_offset += 30  # Increase Y offset for the next line

        back_text = "Press 'b' to go back"
        back_color = main.GREEN if selected_option == len(start_game_menu) else main.WHITE
        main.draw_text(back_text, main.font, back_color, main.SCREEN_WIDTH // 2, 150 + len(main.options_list) * 50)
        pygame.display.update()


def exercise():
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
                    start_game()

        screen.fill(BLACK)

        info_text = ("Hoo....hah.... wow this feels great! I do have some homework to do though...")
        # Split the long text into lines that fit the screen width
        info_lines = textwrap.wrap(info_text, width=60)

        # Display each line of the wrapped text
        y_offset = main.SCREEN_HEIGHT // 4  # Initial Y position for the text
        for line in info_lines:
            main.draw_text(line, main.font, main.WHITE, main.SCREEN_WIDTH // 2, y_offset)
            y_offset += 30  # Increase Y offset for the next line

        back_text = "Press 'b' to go back"
        back_color = main.GREEN if selected_option == len(start_game_menu) else main.WHITE
        main.draw_text(back_text, main.font, back_color, main.SCREEN_WIDTH // 2, 150 + len(main.options_list) * 50)
        pygame.display.update()


def shop():
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
                    start_game()

        screen.fill(BLACK)

        info_text = ("My money...is gone...")
        # Split the long text into lines that fit the screen width
        info_lines = textwrap.wrap(info_text, width=60)

        # Display each line of the wrapped text
        y_offset = main.SCREEN_HEIGHT // 4  # Initial Y position for the text
        for line in info_lines:
            main.draw_text(line, main.font, main.WHITE, main.SCREEN_WIDTH // 2, y_offset)
            y_offset += 30  # Increase Y offset for the next line

        back_text = "Press 'b' to go back"
        back_color = main.GREEN if selected_option == len(start_game_menu) else main.WHITE
        main.draw_text(back_text, main.font, back_color, main.SCREEN_WIDTH // 2, 150 + len(main.options_list) * 50)
        pygame.display.update()


def hang_out():
    running = True
    selected_option = 0
    target_number = random.randint(1, 10)
    guess_input = ""  # Variable to store user input
    correct_guess = None  # Flag to track if the guess is correct or not

    while running:
        screen.fill(BLACK)

        info_text = "I wonder if my friends are free to hang out today! Let's find out..."
        main.draw_text(info_text, main.font, main.WHITE, main.SCREEN_WIDTH // 2, main.SCREEN_HEIGHT // 4)

        info_text1 = "Guess a number between 1 and 10: "
        main.draw_text(info_text1, main.font, main.WHITE, main.SCREEN_WIDTH // 2, main.SCREEN_HEIGHT // 2)

        # Display the guess input box
        pygame.draw.rect(screen, main.WHITE, (main.SCREEN_WIDTH // 2 - 50, main.SCREEN_HEIGHT // 2 + 50, 100, 30))
        main.draw_text(guess_input, main.font, main.BLACK, main.SCREEN_WIDTH // 2, main.SCREEN_HEIGHT // 2 + 65)

        # Display the result if the guess is correct or incorrect
        if correct_guess is not None:
            result_text = "Congratulations! You get to hang out with your friends!" if correct_guess else \
                "Sorry, your friends are busy today. Try again next time."
            main.draw_text(result_text, main.font, main.WHITE, main.SCREEN_WIDTH // 2,
                           main.SCREEN_HEIGHT // 2 + 100)
            pygame.display.update()
            pygame.time.delay(2000)  # Delay for 2 seconds before returning to main menu
            start_game()  # Go back to the main menu after displaying the result
            correct_guess = None  # Reset the flag

        pygame.display.update()

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # Check if Enter key is pressed
                    try:
                        guess = int(guess_input)
                        if 1 <= guess <= 10:
                            if guess == target_number:
                                correct_guess = True  # Set flag for correct guess
                            else:
                                correct_guess = False  # Set flag for incorrect guess
                            guess_input = ""  # Clear the input box
                        else:
                            # Invalid input message
                            result_text = "Invalid input. Please enter a number between 1 and 10."
                            main.draw_text(result_text, main.font, main.RED, main.SCREEN_WIDTH // 2,
                                           main.SCREEN_HEIGHT // 2 + 100)
                            pygame.display.update()
                            pygame.time.delay(2000)  # Delay for 2 seconds before clearing the input box
                            guess_input = ""
                    except ValueError:
                        # Invalid input message
                        result_text = "Invalid input. Please enter a number between 1 and 10."
                        main.draw_text(result_text, main.font, main.RED, main.SCREEN_WIDTH // 2,
                                       main.SCREEN_HEIGHT // 2 + 100)
                        pygame.display.update()
                        pygame.time.delay(2000)  # Delay for 2 seconds before clearing the input box
                        guess_input = ""

                elif event.key == pygame.K_BACKSPACE:  # Check if Backspace key is pressed
                    guess_input = guess_input[:-1]  # Remove the last character from the input
                else:
                    guess_input += event.unicode  # Add typed characters to the input

        # Handle going back
        if pygame.key.get_pressed()[pygame.K_b]:
            main.options()



def party():
    running = True
    clock = pygame.time.Clock()

    start_time = time.time()
    game_duration = 40
    remaining_time = game_duration

    # Platform variables
    platform_width = 100
    platform_height = 20
    platform_color = main.GREEN
    platform_x = main.SCREEN_WIDTH // 2 - platform_width // 2
    platform_y = main.SCREEN_HEIGHT - 40
    platform_speed = 10

    # Falling objects variables
    object_size = 20
    object_color_good = main.GREEN
    object_color_bad = main.RED
    object_speed = 5
    objects = []  # List to store falling objects

    # Points variables
    points = 0
    font_points = pygame.font.Font(None, 24)

    font_timer = pygame.font.Font(None, 24)

    while running:
        screen.fill(main.BLACK)

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Move platform based on keyboard input
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            platform_x -= platform_speed
        if keys[pygame.K_RIGHT]:
            platform_x += platform_speed

        # Ensure platform stays within screen bounds
        platform_x = max(0, min(main.SCREEN_WIDTH - platform_width, platform_x))

        remaining_time = max(0, game_duration - int(time.time() - start_time))

        # Spawn falling objects randomly
        if random.randint(1, 100) == 1:
            object_x = random.randint(0, main.SCREEN_WIDTH - object_size)
            object_y = 0
            is_good = random.choice([True, False])  # Randomly determine if it's a good or bad object
            color = object_color_good if is_good else object_color_bad
            objects.append((object_x, object_y, color, is_good))

        # Create a new list to store updated objects
        updated_objects = []

        # Update falling objects' positions using the original list
        for object_x, object_y, color, is_good in objects:
            object_y += object_speed

            # Check for collision with platform and handle points for good objects
            if object_y + object_size >= platform_y and object_y <= platform_y + platform_height:
                if platform_x <= object_x <= platform_x + platform_width or \
                        platform_x <= object_x + object_size <= platform_x + platform_width:
                    if is_good:
                        points += 1  # Increase points for catching good objects
                    else:
                        points -= 1  # Decrease points for missing bad objects
                else:
                    updated_objects.append((object_x, object_y, color, is_good))  # Add object back to updated list
            elif object_y <= main.SCREEN_HEIGHT:  # Add object back to updated list if it hasn't fallen off
                updated_objects.append((object_x, object_y, color, is_good))

        objects = updated_objects  # Replace original list with updated list

        # Draw platform
        pygame.draw.rect(screen, platform_color, (platform_x, platform_y, platform_width, platform_height))

        # Draw falling objects from the updated list
        for object_x, object_y, color, _ in objects:
            pygame.draw.rect(screen, color, (object_x, object_y, object_size, object_size))

        # Draw points
        points_text = font_points.render(f"Points: {points}", True, main.WHITE)
        screen.blit(points_text, (main.SCREEN_WIDTH - points_text.get_width() - 10, 10))

        #Draw timer
        timer_text = font_timer.render(f"Time: {remaining_time}s", True, main.WHITE)
        screen.blit(timer_text, (10, 10))

        pygame.display.update()
        clock.tick(50)  # Limit frame rate to 30 FPS

        # Game over condition (time runs out)...
        if time.time() - start_time >= game_duration:
            running = False
            return False


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
