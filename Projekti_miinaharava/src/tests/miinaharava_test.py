import unittest
import pygame
from miinaharava import Miinaharava


class TestMiinaharava(unittest.TestCase):
    def setUp(self):
        self._game = Miinaharava()

    def test_opens_menu_when_no_events(self):
        self._game.events()

        self.assertTrue(self._game.open_menu)

    """
    def test_opens_game_with_no_settings(self):
        self._game.events()
        pygame.mouse.set_pos([720/3, 150])
        mouse_pos = [720/3, 150]
        StubEvent(pygame.MOUSEBUTTONDOWN, mouse_pos)
        self._game._menu.events()
        pygame.time.delay(500)

        self.assertEqual(self._game._game.gridsize, 10)
    """