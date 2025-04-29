import unittest
import numpy as np
import pandas as pd
from simulator.dice import Die
from game import Game
from simulator.analyzer import Analyzer

class TestAnalyzer(unittest.TestCase):
    """Unit tests for the Analyzer class"""
    
    def setUp(self):
        """Set up test fixtures"""
        # Create a game with two dice
        faces = np.array(['A', 'B', 'C', 'D', 'E', 'F'])
        die1 = Die(faces)
        die2 = Die(faces)
        self.game = Game([die1, die2])
        self.game.play(10)  # Play 10 rolls
        self.analyzer = Analyzer(self.game)
        
    def test_init_valid(self):
        """Test analyzer initialization with valid game object"""
        self.assertIsInstance(self.analyzer.game, Game)
        
    def test_init_invalid(self):
        """Test analyzer initialization with invalid input"""
        with self.assertRaises(ValueError):
            Analyzer("not a game object")
            
    def test_jackpot(self):
        """Test jackpot counting method"""
        jackpots = self.analyzer.jackpot()
        self.assertIsInstance(jackpots, int)
        self.assertTrue(jackpots >= 0)
        
    def test_face_counts_per_roll(self):
        """Test face counts per roll method"""
        counts = self.analyzer.face_counts_per_roll()
        
        # Verify output format
        self.assertIsInstance(counts, pd.DataFrame)
        self.assertEqual(len(counts), 10)  # Should have 10 rolls
        
        # Verify that sum of counts per row equals number of dice
        row_sums = counts.sum(axis=1)
        self.assertTrue(all(row_sums == 2))  # 2 dice per roll
        
    def test_combo_count(self):
        """Test combination counting method"""
        combos = self.analyzer.combo_count()
        
        # Verify output format
        self.assertIsInstance(combos, pd.DataFrame)
        self.assertTrue(isinstance(combos.index, pd.MultiIndex))
        self.assertEqual(len(combos.columns), 1)  # Should have one 'Count' column
        
        # Verify counts are non-negative
        self.assertTrue(all(combos['Count'] > 0))
        
    def test_permutation_count(self):
        """Test permutation counting method"""
        perms = self.analyzer.permutation_count()
        
        # Verify output format
        self.assertIsInstance(perms, pd.DataFrame)
        self.assertTrue(isinstance(perms.index, pd.MultiIndex))
        self.assertEqual(len(perms.columns), 1)  # Should have one 'Count' column
        
        # Verify counts are non-negative
        self.assertTrue(all(perms['Count'] > 0))
        
        # Verify permutations count is >= combinations count
        # (since order matters in permutations)
        self.assertTrue(len(perms) >= len(self.analyzer.combo_count()))

if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=2, exit=False)