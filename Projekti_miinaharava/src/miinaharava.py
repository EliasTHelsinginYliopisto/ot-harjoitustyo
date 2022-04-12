import sys
import pygame
from mainmenu import MainMenu


class Miinaharava:
    def __init__(self):

        self._menu = MainMenu()
        self.open_menu = False
        self.exit_game = False
        self.running = False

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.exit_game = True
            else:
                self.open_menu = True

    def run(self):
        pygame.display.set_caption("Miinaharava")
        self.running = True

        while self.running:
            self.events()

            if self.exit_game:
                sys.exit()
            elif self.open_menu:
                self._menu.run()
            pygame.display.update()
