import unittest
import pygame
from miinaharava import Miinaharava


class TestMiinaharava(unittest.TestCase):
    def setUp(self):
        self._game = Miinaharava()

    def test_opens_menu_when_no_events(self):
        self._game.events()

        self.assertTrue(self._game.open_menu)
