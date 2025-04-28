import unittest
import numpy as np
import pandas as pd
from die.dice import Die
from game.game import Game

class TestGame(unittest.TestCase):
    """Unit tests for the Game class"""
    
    def setUp(self):
        """Set up test fixtures"""
        # Create two similar dice
        faces = np.array(['A', 'B', 'C', 'D', 'E', 'F'])
        self.die1 = Die(faces)
        self.die2 = Die(faces)
        self.dice_list = [self.die1, self.die2]
        self.game = Game(self.dice_list)
        
    def test_init(self):
        """Test game initialization"""
        self.assertEqual(len(self.game.dice), 2)
        self.assertIsInstance(self.game.dice[0], Die)
        self.assertIsInstance(self.game.dice[1], Die)
        
    def test_play(self):
        """Test playing the game"""
        n_rolls = 3
        self.game.play(n_rolls)
        results = self.game.show_outcome()
        
        # Check if results DataFrame has correct shape and format
        self.assertIsInstance(results, pd.DataFrame)
        self.assertEqual(len(results), n_rolls)  # Correct number of rolls
        self.assertEqual(len(results.columns), len(self.dice_list))  # Correct number of dice
        
    def test_show_outcome_wide(self):
        """Test showing results in wide format"""
        self.game.play(3)
        results = self.game.show_outcome("wide")
        
        # Check wide format properties
        self.assertIsInstance(results, pd.DataFrame)
        self.assertEqual(len(results.columns), len(self.dice_list))
        
    def test_show_outcome_narrow(self):
        """Test showing results in narrow format"""
        self.game.play(3)
        results = self.game.show_outcome("narrow")
        
        # Check narrow format properties
        self.assertIsInstance(results, pd.DataFrame)
        self.assertEqual(len(results.columns), 1)  # Should have single column for outcomes
        self.assertTrue(isinstance(results.index, pd.MultiIndex))  # Should have MultiIndex
        
    def test_show_outcome_invalid(self):
        """Test showing results with invalid format"""
        self.game.play(3)
        with self.assertRaises(ValueError):
            self.game.show_outcome("invalid_format")

if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=2, exit=False)