import pygame

class DefineColours():
    def __init__(self):
        self.BLACK = (0,0,0)
        self.DARK_GREY = (96,96,96)
        self.LIGHT_GREY = (160,160,160)




class GameTheme():
    def __init__(self):
        self._define = DefineColours()

        self.background_colour = self._define.BLACK

        self.text_colour = self._define.DARK_GREY

        self.button_colour = self._define.LIGHT_GREY

        self.text_font = pygame.font.SysFont('Arial',40)

        self.title_font = pygame.font.SysFont('Arial',100)