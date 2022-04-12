import pygame


class Button():
    def __init__(self, x_coord, y_coord, size, surface, colour):
        self.rect = pygame.draw.rect(
            surface, colour, pygame.Rect((x_coord, y_coord), (100*size, 50*size)))
