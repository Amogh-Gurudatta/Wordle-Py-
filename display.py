import pygame
import sys
import wordle

pygame.init()

WIDTH, HEIGHT = 633, 900

DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT))
BACKGROUND = pygame.image.load("Starting Tiles.png")
BG_RECTANGLE = BACKGROUND.get_rect(center=(317, 300))
ICON = pygame.image.load("wordle-icon.svg")

pygame.display.set_caption("Wordle")
pygame.display.set_icon(ICON)

GREY = "#3A3A3C"
YELLOW = "#B59F3B"
GREEN = "#538D4E"
BORDER = "#D3D6DA"
FILLED_BORDER = "#878A8C"

KEYBOARD_LIST = ["QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM"]

GUESSED_ALPHABET_FONT = pygame.font.Font("FreeSansBold.otf", 50)
FREE_ALPHABET_FONT = pygame.font.Font("FreeSansBold.otf", 25)

DISPLAY.fill("#FFFFFF")
DISPLAY.blit(BACKGROUND, BG_RECTANGLE)
pygame.display.update()

ALPHABET_X_DISTANCE = 85
ALPHABET_Y_DISTANCE = 12
ALPHABET_SIZE = 75

current_alphabet_bg_x = 110

keyboard_indicator = []


class Letter:
    def __init__(self, text, bg_pos):
        self.bg_colour = "#FFFFFF"
        self.txt_colour = "#000000"
        self.bg_pos = bg_pos
        self.bg_x = bg_pos[0]
        self.bg_y = bg_pos[0]
        self.bg_rect = (bg_pos[0], self.bg_y, ALPHABET_SIZE, ALPHABET_SIZE)
        self.txt = text
        self.txt_pos = (self.bg_x + 36, bg_pos[1] + 34)
        self.txt_surface = GUESSED_ALPHABET_FONT.render(self.txt, True, self.txt_colour)
        self.txt_rect = self.txt_surface.get_rect(center=self.txt_pos)

    def draw(self):
        pygame.draw.rect(DISPLAY, self.bg_colour, self.bg_rect)

        if self.bg_colour == "#FFFFFF":
            pygame.draw.rect(DISPLAY, FILLED_BORDER, self.bg_rect, 3)

        self.text_surface = GUESSED_ALPHABET_FONT.render(
            self.text, True, self.txt_colour
        )
        DISPLAY.blit(self.text_surface, self.txt_rect)
        pygame.display.update()

    def delete(self):
        pygame.draw.rect(DISPLAY, "#FFFFFF", self.bg_rect)
        pygame.draw.rect(DISPLAY, BORDER, self.bg_rect, 3)
        pygame.display.update()


class Indicator:
    def __init__(self, x, y, letter):
        pass

    def draw(self):
        pass


def check_guess():
    pass


def play_again():
    pass


def reset():
    pass


def create_new_letter():
    pass


def delete_letter():
    pass


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
