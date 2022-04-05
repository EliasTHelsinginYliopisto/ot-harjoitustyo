import pygame

class Button():
    def __init__(self, x, y, size, surface, colour):
        self.rect = pygame.draw.rect(surface, colour, pygame.Rect((x,y)(100*size,50*size)))