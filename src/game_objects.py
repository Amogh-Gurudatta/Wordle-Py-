import pygame
from constants import *
import display


class Letter:
    def __init__(self, txt, bg_pos):
        self.bg_colour = WHITE
        self.txt_colour = BLACK
        self.bg_pos = bg_pos
        self.bg_x = bg_pos[0]
        self.bg_y = bg_pos[1]
        self.bg_rect = (bg_pos[0], self.bg_y, LETTER_SIZE, LETTER_SIZE)
        self.txt = txt
        self.txt_pos = (self.bg_x + 36, bg_pos[1] + 34)
        self.txt_surface = GUESSED_LETTER_FONT.render(self.txt, True, self.txt_colour)
        self.txt_rect = self.txt_surface.get_rect(center=self.txt_pos)

    def draw(self):
        pygame.draw.rect(display.DISPLAY, self.bg_colour, self.bg_rect)

        if self.bg_colour == WHITE:
            pygame.draw.rect(display.DISPLAY, FILLED_BORDER, self.bg_rect, 3)

        self.txt_surface = GUESSED_LETTER_FONT.render(self.txt, True, self.txt_colour)
        display.DISPLAY.blit(self.txt_surface, self.txt_rect)
        pygame.display.update()

    def delete(self):
        pygame.draw.rect(display.DISPLAY, WHITE, self.bg_rect)
        pygame.draw.rect(display.DISPLAY, BORDER, self.bg_rect, 3)
        pygame.display.update()


class Indicator:
    def __init__(self, x, y, letter):
        self.x = x
        self.y = y
        self.text = letter
        self.rect = (self.x, self.y, 57, 75)
        self.bg_colour = BORDER

    def draw(self):
        pygame.draw.rect(display.DISPLAY, self.bg_colour, self.rect)
        self.text_surface = AVAILABLE_LETTER_FONT.render(self.text, True, WHITE)
        self.text_rect = self.text_surface.get_rect(center=(self.x + 27, self.y + 30))
        display.DISPLAY.blit(self.text_surface, self.text_rect)
        pygame.display.update(self.rect)
