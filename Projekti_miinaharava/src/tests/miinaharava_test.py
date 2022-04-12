import unittest
from miinaharava import Miinaharava


class TestMiinaharava(unittest.TestCase):
    def setUp(self):
        self.game = Miinaharava()

    def test_opens_menu_when_no_events(self):
        self.game.events()

        self.assertTrue(self.game.open_menu)
