import pygame


class DefineColours():
    """Luokka, joka määrittää värit teema luokkaa varten"""

    def __init__(self):
        self.black = (0, 0, 0)
        self.dark_grey = (96, 96, 96)
        self.light_grey = (160, 160, 160)
        self.white = (255, 255, 255)


class GameTheme():
    """Luokka joka määrittää värit ja fontit peliä varten

    Attributes:
        define: teeman värit"""

    def __init__(self):
        self._define = DefineColours()

        self.background_colour = self._define.black

        self.text_colour = self._define.dark_grey

        self.button_colour = self._define.light_grey

        self.closed_colour = self._define.white

        self.text_font = pygame.font.SysFont('Arial', 40)

        self.mines_font = pygame.font.SysFont('Arial', 20)

        self.title_font = pygame.font.SysFont('Arial', 100)
