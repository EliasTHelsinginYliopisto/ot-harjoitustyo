import sys
import pygame
from mainmenu import MainMenu
from gameinstance import GameLogic


class Miinaharava:
    """pelin pääluokka, joka kutsuu alaluokkia
    
    Attributes:
        menu: pelin päävalikko
        game: pelin logiikka
        open_menu: onko peli käynnissä
        exit_game: suljetaanko sovellus
        start_game: käynnistetäänkö peli annetuilla asetuksilla
        running: onko sovellus käynnissä
    """


    def __init__(self):
        """luokan konstruktori"""

        self._menu = MainMenu()
        self._game = GameLogic()
        self.open_menu = False
        self.exit_game = False
        self.start_game = False
        self.running = False

    def events(self):
        """Sulkee pelin"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.exit_game = True
            else:
                self.open_menu = True

    def run(self):
        """pääluokan suoritus
        
        Args:
            status:
            luokkien palauttamat tiedot. menu palauttaa pelin asetukset,
            pelin logiikka palauttaa palataanko menuun
        """
        pygame.display.set_caption("Miinaharava")
        self.running = True

        while self.running:
            self.events()

            if self.exit_game:
                sys.exit()
            elif self.open_menu:
                status = self._menu.run()
                if isinstance(status, list):
                    self.open_menu = False
                    self.start_game = True
                elif status == 'quit_game':
                    pygame.quit()

            elif self.start_game:
                status = self._game.run(status)
                if status == 'return_to_menu':
                    self.start_game = False

            pygame.display.update()
