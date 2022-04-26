import unittest
import pygame
from gameinstance import GameLogic

class TestMiinaharava(unittest.TestCase):
    def setUp(self):
        self._game = GameLogic()

    def test_starts_without_settings(self):
        self._game.apply_settings(['', ''])
        self.assertEqual(self._game.gridsize, 10)
        self.assertEqual(self._game.mineamount, 20)

    def test_creates_grid_correctly(self):
        self._game.gridsize = 5
        grid1 = self._game.create_grid()
        grid2 = [[[0, 'closed'], [0, 'closed'], [0, 'closed'], [0, 'closed'], [0, 'closed']], 
        [[0, 'closed'], [0, 'closed'], [0, 'closed'], [0, 'closed'], [0, 'closed']], 
        [[0, 'closed'], [0, 'closed'], [0, 'closed'], [0, 'closed'], [0, 'closed']], 
        [[0, 'closed'], [0, 'closed'], [0, 'closed'], [0, 'closed'], [0, 'closed']], 
        [[0, 'closed'], [0, 'closed'], [0, 'closed'], [0, 'closed'], [0, 'closed']]]
        self.assertEqual(grid1, grid2)
    
    '''
    def test_sets_correct_amount_of_mines(self):
        self._game.gridsize = 20
        self._game.mineamount = 100
        self._game.minefield = self._game.create_grid()
        start = [0, 0]
        self._game.set_mines(start)

        in_grid = 0
        for i in self._game.minefield:
            for j in i:
                if j[0] == 'M':
                    in_grid += 1
        self.assertEqual(self._game.mineamount, in_grid)
    '''

    def test_sets_correct_a_mine(self):
        self._game.gridsize = 5
        self._game.mineamount = 1
        self._game.minefield = self._game.create_grid()
        start = [0, 0]
        self._game.set_mines(start)

        in_grid = 0
        for i in self._game.minefield:
            for j in i:
                if j[0] == 'M':
                    in_grid += 1
        self.assertEqual(self._game.mineamount, in_grid)

    def test_opening_square_sets_square_open(self):
        self._game.gridsize = 1
        self._game.in_progress = True
        self._game.minefield = self._game.create_grid()
        self._game.reveal_square(0, 0)

        self.assertEqual(self._game.user_interface[2], 10)