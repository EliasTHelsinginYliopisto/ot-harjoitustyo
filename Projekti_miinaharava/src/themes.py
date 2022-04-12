import pygame


class DefineColours():
    def __init__(self):
        self.black = (0, 0, 0)
        self.dark_grey = (96, 96, 96)
        self.light_grey = (160, 160, 160)


class GameTheme():
    def __init__(self):
        self._define = DefineColours()

        self.background_colour = self._define.black

        self.text_colour = self._define.dark_grey

        self.button_colour = self._define.light_grey

        self.text_font = pygame.font.SysFont('Arial', 40)

        self.title_font = pygame.font.SysFont('Arial', 100)
