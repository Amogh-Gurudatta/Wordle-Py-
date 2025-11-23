import pygame
from constants import *

DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT))

try:
    BACKGROUND = pygame.image.load(os.path.join(ASSET_PATH, "Starting Tiles.png"))
    ICON = pygame.image.load(os.path.join(ASSET_PATH, "Icon.svg"))
    BG_RECT = BACKGROUND.get_rect(center=(317, 300))
except pygame.error as e:
    print(f"Error loading assets: {e}")
    exit()

pygame.display.set_caption("Wordle!")
pygame.display.set_icon(ICON)

def init_screen():
    """Draws empty white board."""
    DISPLAY.fill(WHITE)
    DISPLAY.blit(BACKGROUND, BG_RECT)
    pygame.display.update()


def init_indicators():
    from game_objects import Indicator
    indicators = []
    indicator_x, indicator_y = 20, 600
    for i in range(3):
        for letter in ALPHABET[i]:
            new_indicator = Indicator(indicator_x, indicator_y, letter)
            indicators.append(new_indicator)
            new_indicator.draw()
            indicator_x += 60
        indicator_y += 100
        if i == 0:
            indicator_x = 50
        elif i == 1:
            indicator_x = 105
    return indicators


def update_guess_colours(current_guess, tile_colour):
    """Updates Colour of tiles after guess."""
    for i in range(5):
        current_guess[i].bg_colour = tile_colour[i]
        current_guess[i].txt_colour = WHITE
        current_guess[i].draw()


def update_keyboard(indicators, key_colours):
    for letter, colour in key_colours.items():
        for indicator in indicators:
            if indicator.text == letter:
                # Logic to prevent downgrading colours
                if indicator.bg_colour == GREEN:
                    continue
                if indicator.bg_colour == YELLOW and colour == GREY:
                    continue
                indicator.bg_colour = colour
                indicator.draw()


def draw_play_again(stats, SECRET):
    """Displays the end-game screen with stats and play-again prompt."""
    pygame.draw.rect(DISPLAY, WHITE, (10, 600, 1000, 600))

    play_again_text = PLAY_AGAIN_FONT.render("Press ENTER to Play Again!", True, BLACK)
    play_again_rect = play_again_text.get_rect(center=(WIDTH / 2, 850))

    word_was_text = PLAY_AGAIN_FONT.render(f"The word was {SECRET}!", True, BLACK)
    word_was_rect = word_was_text.get_rect(center=(WIDTH / 2, 800))

    DISPLAY.blit(word_was_text, word_was_rect)
    DISPLAY.blit(play_again_text, play_again_rect)

    # --- Display Statistics ---
    wins_text = STATS_FONT.render(f"Wins: {stats['wins']}", True, BLACK)
    losses_text = STATS_FONT.render(f"Losses: {stats['losses']}", True, BLACK)
    curr_streak_text = STATS_FONT.render(
        f"Current Streak: {stats['current_streak']}", True, BLACK
    )
    max_streak_text = STATS_FONT.render(
        f"Max Streak: {stats['max_streak']}", True, BLACK
    )

    DISPLAY.blit(wins_text, (WIDTH / 2 - 250, 650))
    DISPLAY.blit(losses_text, (WIDTH / 2 - 250, 680))
    DISPLAY.blit(curr_streak_text, (WIDTH / 2 + 50, 650))
    DISPLAY.blit(max_streak_text, (WIDTH / 2 + 50, 680))

    dist_title = STATS_FONT.render("Guess Distribution:", True, BLACK)
    DISPLAY.blit(dist_title, (WIDTH / 2 - 100, 720))
    for i in range(1, 7):
        dist_text = STATS_FONT.render(
            f"{i}: {stats['guess_distribution'][str(i)]}", True, GREY
        )
        DISPLAY.blit(dist_text, (WIDTH / 2 - 10, 720 + i * 20))

    pygame.display.update()


def reset_display(indicators):
    init_screen()
    for indicator in indicators:
        indicator.bg_colour = BORDER
        indicator.draw()


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
