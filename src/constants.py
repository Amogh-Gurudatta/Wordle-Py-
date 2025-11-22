import pygame
import os
import random

pygame.init()
pygame.font.init()

# File Paths
ASSET_PATH = "assets"
DATA_PATH = "data"
WORDS_FILE = os.path.join(DATA_PATH, "words.txt")
STATS_FILE = os.path.join(DATA_PATH, "stats.json")

# Dimensions
WIDTH, HEIGHT = 633, 900
LETTER_SIZE = 75
ALPHABET_X_DISTANCE = 85
ALPHABET_Y_DISTANCE = 12

# Screen & Icon
# DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT))
# try:
#     BACKGROUND = pygame.image.load(os.path.join(ASSET_PATH, "Starting Tiles.png"))
#     ICON = pygame.image.load(os.path.join(ASSET_PATH, "Icon.svg"))
# except pygame.error as e:
#     print(f"Error loading assets: {e}")
#     print(
#         "Please make sure the 'assets' folder is in the same directory and contains 'Starting Tiles.png' and 'Icon.svg'"
#     )
#     pygame.quit()
#     exit()

# BG_RECT = BACKGROUND.get_rect(center=(317, 300))
# pygame.display.set_caption("Wordle!")
# pygame.display.set_icon(ICON)

# --- Colours ---
GREY = "#3A3A3C"
YELLOW = "#B59F3B"
GREEN = "#538D4E"
BORDER = "#D3D6DA"
FILLED_BORDER = "#878A8C"
BLACK = "#000000"
WHITE = "#FFFFFF"

# --- Fonts ---
try:
    FONT_PATH = os.path.join(ASSET_PATH, "FreeSansBold.otf")
    GUESSED_LETTER_FONT = pygame.font.Font(FONT_PATH, 50)
    AVAILABLE_LETTER_FONT = pygame.font.Font(FONT_PATH, 25)
    PLAY_AGAIN_FONT = pygame.font.Font(FONT_PATH, 40)
    STATS_FONT = pygame.font.Font(FONT_PATH, 20)
except FileNotFoundError:
    print(f"Error: Font file '{FONT_PATH}' not found.")
    print("Please ensure the font file is in the 'assets' directory.")
    pygame.quit()
    exit()

# --- Keyboard Layout ---
ALPHABET = ["QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM"]
VALID_KEYS = "QWERTYUIOPASDFGHJKLZXCVBNM"

# DISPLAY.fill("#FFFFFF")
# DISPLAY.blit(BACKGROUND, BG_RECT)
# pygame.display.update()

# def get_word():
#     try:
#         with open(WORDS_FILE, "r") as f:
#             # Read all text and split into words by whitespace
#             words = f.read().split()
#         if not words:
#             raise ValueError("Words file is empty.")
#         # Return a random word from the list
#         return set(words), random.choice(words)
#     except FileNotFoundError:
#         print(f"Error: '{WORDS_FILE}' not found. Please create it.")
#         exit()
#     except Exception as e:
#         print(f"Error loading words: {e}")
#         exit()
        
# WORDS, SECRET = get_word()