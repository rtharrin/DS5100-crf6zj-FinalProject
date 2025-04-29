import unittest
import numpy as np
import pandas as pd
from montecarlo.simulator import Die
from montecarlo.simulator import Game
from montecarlo.simulator import Analyzer

class TestDie(unittest.TestCase):
    """Unit tests for the Die class"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.faces = np.array(['A', 'B', 'C', 'D', 'E', 'F'])
        self.die = Die(self.faces)
        
    def test_init_valid(self):
        """Test initialization with valid input"""
        self.assertIsInstance(self.die.show_die(), pd.DataFrame)
        self.assertEqual(len(self.die.show_die()), len(self.faces))
        
    def test_init_invalid_type(self):
        """Test initialization with invalid input type"""
        with self.assertRaises(TypeError):
            Die([1, 2, 3, 4, 5, 6])  # List instead of numpy array
            
    def test_init_non_unique(self):
        """Test initialization with non-unique faces"""
        with self.assertRaises(ValueError):
            Die(np.array(['A', 'B', 'C', 'C', 'D']))  # Duplicate face
            
    def test_change_weight_valid(self):
        """Test changing weight with valid inputs"""
        self.die.change_weight('A', 2.0)
        self.assertEqual(self.die.show_die().loc['A', 'Weight'], 2.0)
        
    def test_change_weight_invalid_face(self):
        """Test changing weight with invalid face"""
        with self.assertRaises(IndexError):
            self.die.change_weight('X', 2.0)  # Face doesn't exist
            
    def test_change_weight_invalid_weight(self):
        """Test changing weight with invalid weight type"""
        with self.assertRaises(TypeError):
            self.die.change_weight('A', 'heavy')  # Non-numeric weight
            
    def test_roll_die_single(self):
        """Test rolling die once"""
        result = self.die.roll_die()
        self.assertEqual(len(result), 1)
        self.assertIn(result[0], self.faces)
        
    def test_roll_die_multiple(self):
        """Test rolling die multiple times"""
        n_rolls = 5
        result = self.die.roll_die(n_rolls)
        self.assertEqual(len(result), n_rolls)
        self.assertTrue(all(face in self.faces for face in result))
        
    def test_show_die(self):
        """Test showing die state"""
        df = self.die.show_die()
        self.assertIsInstance(df, pd.DataFrame)
        self.assertTrue('Weight' in df.columns)
        self.assertEqual(len(df), len(self.faces))
        self.assertTrue(all(face in df.index for face in self.faces))

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
