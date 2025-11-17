import pygame
import sys
from constants import *
from game_objects import Indicator


def init_screen():
    """Draws empty white board."""
    DISPLAY.fill(WHITE)
    DISPLAY.blit(BACKGROUND, BG_RECT)
    pygame.display.update()


def init_indicators():
    indicators = []
    return indicators


def update_guess_colours(current_guess, tile_colour):
    """Updates Colour of tiles after guess."""
    for i in range(5):
        current_guess[i].bg_colour = tile_colour[i]
        current_guess[i].txt_colour = WHITE
        current_guess[i].draw()


def update_keyboard(indicators, key_colours):
    pass


def draw_play_again():
    pass


def reset_display():
    pass


# def create_new_letter():
#     global current_guess_string, current_alphabet_bg_x

#     current_guess_string += key_pressed
#     new_letter = Letter(
#         key_pressed,
#         (current_alphabet_bg_x, guess_count * 100 + ALPHABET_Y_DISTANCE),
#     )
#     current_alphabet_bg_x += ALPHABET_X_DISTANCE
#     guesses[guess_count].append(new_letter)
#     current_guess.append(new_letter)
#     for guess in guesses:
#         for letter in guess:
#             letter.draw()


def delete_letter():
    global current_guess_string, current_alphabet_bg_x

    guesses[guess_count][-1].delete()
    guesses[guess_count].pop()
    current_guess_string = current_guess_string[:-1]
    current_guess.pop()
    current_alphabet_bg_x -= ALPHABET_X_DISTANCE


# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()

#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_RETURN:
#                 if game_result != "":
#                     reset()
#                 else:
#                     if isValid(current_guess_string):
#                         check_guess(current_guess)

#             elif event.key == pygame.K_BACKSPACE:
#                 if len(current_guess_string) > 0:
#                     delete_letter()
#             else:
#                 key_pressed = event.unicode.upper()
#                 if key_pressed in "QWERTYUIOPASDFGHJKLZXCVBNM" and key_pressed != "":
#                     if len(current_guess_string) < 5:
#                         create_new_letter()
