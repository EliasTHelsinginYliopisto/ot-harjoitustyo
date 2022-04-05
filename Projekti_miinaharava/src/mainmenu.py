import pygame
from themes import GameTheme
from buttons import Button

window_size_x = 720
window_size_y = 480

pygame.init()

window = pygame.display.set_mode(window_size_x,window_size_y)

pygame.display.set_caption("Miinaharava")

run = True
while run:


    pygame.display.update()

pygame.quit()