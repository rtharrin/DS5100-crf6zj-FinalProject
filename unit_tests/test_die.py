import unittest
import numpy as np
import pandas as pd
from die.dice import Die

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

if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=2, exit=False)