"""
Unit tests for the Bowling Game

This module contains basic unit tests for the BowlingGame class.
Students should expand these tests to cover all functionality and edge cases.
"""

import unittest
from bowling_game import BowlingGame


class TestBowlingGame(unittest.TestCase):
    def setUp(self):
        """Set up a new game before each test."""
        self.game = BowlingGame()

    def roll_many(self, n, pins):
        """Helper to roll the same number of pins multiple times."""
        for _ in range(n):
            self.game.roll(pins)

    def test_gutter_game(self):
        """Test a game where no pins are knocked down."""
        self.roll_many(20, 0)
        self.assertEqual(0, self.game.score())

    def test_all_ones(self):
        """Test a game where one pin is knocked down on each roll."""
        self.roll_many(20, 1)
        # Expected score: 20 (1 pin × 20 rolls)
        self.assertEqual(20, self.game.score())

    def test_single_strike(self):
        """Test that a single strike is scored correctly
        Strike +> 10 and next 2 rolls as a bonmus"""
        self.game.roll(10)
        self.game.roll(3)
        self.game.roll(4)
        self.roll_many(16, 0)
        # Frame 1: 10 + 3 + 4 = 17, Frame 2: 3 + 4 = 7, total = 24
        self.assertEqual(24, self.game.score())


    def test_two_consecutive_strikes(self):
        """
        Test that 2 strikes in a row are scored correctly
        """
        self.game.roll(10)
        self.game.roll(10)

        self.game.roll(3)
        self.game.roll(4)
        self.roll_many(14, 0)
        self.assertEqual(47, self.game.score())

    def test_single_spare(self):

        """ Test that a single spare is scored corectly
        Spare => 10 plus next roll as a bonus"""

        self.game.roll(5)
        self.game.roll(5) 

        self.game.roll(3)
        self.roll_many(17, 0)
        self.assertEqual(16, self.game.score())

    def test_two_consecutive_spares(self):
        """ Test that two spares in a row will be scored correctly """

        self.game.roll(7)
        self.game.roll(3)

        self.game.roll(6)
        self.game.roll(4)

        self.game.roll(3)
        self.roll_many(15, 0)
        self.assertEqual(32, self.game.score())

    
    def test_10th_frame_strike(self):
        """Test getting a strkie in the 10th frame,
          this gives the player 2 bonus rolls """
        
        self.roll_many(18, 0)

        self.game.roll(10)
        self.game.roll(3)
        self.game.roll(4)
        self.assertEqual(17, self.game.score())


    def test_10th_frame_spare(self): 
        """ Test getting a spare in the 10th frame.
            this gives the player 1 bonus roll"""
        
        self.roll_many(18, 0)

        self.game.roll(7)
        self.game.roll(3)
        self.game.roll(4)
        self.assertEqual(14, self.game.score())

   
    def test_all_strikes(self):
        """Test to check a perfect game, 12 strikes"""

        for _ in range(12):
            self.game.roll(10) 

        self.assertEqual(300, self.game.score())






    


if __name__ == "__main__":
    unittest.main()