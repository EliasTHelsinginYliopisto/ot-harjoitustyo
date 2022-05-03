import unittest
import pygame
from gameinstance import GameLogic
import sys


class TestMiinaharava(unittest.TestCase):
    def setUp(self):
        self._game = GameLogic()
        self._game.window = pygame.display.set_mode(
            (1000, 1000)
        )

    def test_starts_without_settings(self):
        self._game.apply_settings(['', ''])
        self.assertEqual(self._game.gridsize, 10)
        self.assertEqual(self._game.mineamount, 20)

    def test_creates_grid_correctly(self):
        self._game.gridsize = 5
        grid1 = self._game.create_grid()
        grid2 = [[[0, 'closed'], [0, 'closed'], [0, 'closed'], [0, 'closed'], [0, 'closed']],
                 [[0, 'closed'], [0, 'closed'], [0, 'closed'],
                     [0, 'closed'], [0, 'closed']],
                 [[0, 'closed'], [0, 'closed'], [0, 'closed'],
                     [0, 'closed'], [0, 'closed']],
                 [[0, 'closed'], [0, 'closed'], [0, 'closed'],
                  [0, 'closed'], [0, 'closed']],
                 [[0, 'closed'], [0, 'closed'], [0, 'closed'], [0, 'closed'], [0, 'closed']]]
        self.assertEqual(grid1, grid2)

    def test_sets_correct_amount_of_mines(self):
        self._game.gridsize = 10
        self._game.mineamount = 91
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
        self._game.window = pygame.display.set_mode(
            (1000, 1000)
        )
        self._game.reveal_square(0, 0)

        self.assertEqual(self._game.user_interface[2], 10)
   
   
    def test_opening_mine_ends_game(self):
        self._game.gridsize = 1
        self._game.in_progress = True
        self._game.minefield = [[['M', 'closed']]]
        self._game.reveal_square(0, 0)

        self.assertEqual(self._game.running, False)
    

    def test_end_gives_flagging_bonus(self):
        self._game.gridsize = 1
        self._game.in_progress = True
        self._game.minefield = [[['M', 'flagged']]]
        self._game.end_game()
        
        self.assertEqual(self._game.user_interface[2], 100)
    
    def test_can_set_flags(self):
        self._game.gridsize = 1
        self._game.in_progress = True
        self._game.minefield = [[['M', 'closed']]]
        self._game.set_flag(0, 0)

        self.assertEqual(self._game.minefield, [[['M', 'flagged']]])

    
    """
    def test_game_runs_without_settings(self):
        self._game.run(['', ''])    #gets stuck running game 
        self.assertEqual(self._game.mineamount, 20)
    """

