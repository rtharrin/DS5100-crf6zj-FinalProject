import unittest
import numpy as np
import pandas as pd
from montecarlo.simulator import Die
from montecarlo.simulator import Game
from montecarlo.simulator import Analyzer



class TestSimulator(unittest.TestCase):
    """Unit tests for the project"""
    
    def test_1_die_init(self):
        """Test initialization with valid input"""
        faces = np.array(['A', 'B', 'C', 'D', 'E', 'F'])
        die1 = Die(faces)
        #check that it is a dataframe of the correct number of entries
        self.assertIsInstance(die1.df, pd.DataFrame)
        self.assertEqual(len(die1.df), len(faces))
    
    def test_2_die_change_weight(self):
        """Test changing weight of a die"""
        faces = np.array(['A', 'B', 'C', 'D', 'E', 'F'])
        die2 = Die(faces)
        
        #change the weight of face 'F' to 9.0 and make sure it updated
        die2.change_weight('F', 9.0)
        self.assertEqual(die2.df.loc['F', 'Weight'], 9.0)
    
    def test_3_die_roll_die(self):
        """Test rolling a die"""
        faces = np.array(['A', 'B', 'C', 'D', 'E', 'F'])
        die3 = Die(faces)
        
        #roll the die 10 times and check that the result is a list of length 10
        results = die3.roll_die(10)
        self.assertIsInstance(results, list)
        self.assertEqual(len(results), 10)
    
    def test_4_die_show_die(self):
        """Test showing the die"""
        faces = np.array(['A', 'B', 'C', 'D', 'E', 'F'])
        die4 = Die(faces)
        
        #make sure a dataframe is returned
        self.assertIsInstance(die4.show_die(), pd.DataFrame)
    
    def test_5_game_init(self):
        """Test initialization with valid input"""
        faces = np.array(['A', 'B', 'C', 'D', 'E', 'F'])
        die5 = Die(faces)
        game1 = Game([die5])
        
        #check that it is a Game object with correct number of dice
        self.assertIsInstance(game1, Game)
        self.assertEqual(len(game1.dice), 1)
    
    def test_6_game_play(self):
        """Test playing a game"""
        faces = np.array(['A', 'B', 'C', 'D', 'E', 'F'])
        die6 = Die(faces)
        game2 = Game([die6])
        
        #play the game and check that the outcome is a DataFrame with expected shape
        game2.play(10)
        self.assertIsInstance(game2.show_outcome(), pd.DataFrame)
        self.assertEqual(game2.show_outcome().shape[0], 10)
        self.assertEqual(game2.show_outcome().shape[1], 1)
    
    def test_7_game_show_outcome(self):
        """Test showing the outcome of a game"""
        faces = np.array(['A', 'B', 'C', 'D', 'E', 'F'])
        die7 = Die(faces)
        game3 = Game([die7])
        
        #play the game and check that the outcome is a DataFrame
        game3.play(10)
        self.assertIsInstance(game3.show_outcome("wide"), pd.DataFrame)
        #Make sure narrow has multiindex
        self.assertIsInstance(game3.show_outcome("narrow").index, pd.MultiIndex)
    
    def test_8_analyzer_init(self):
        """Test initialization of Analyzer with valid input"""
        faces = np.array(['A', 'B', 'C', 'D', 'E', 'F'])
        die8 = Die(faces)
        game4 = Game([die8])
        analyzer1 = Analyzer(game4)
        
        #check that it is an Analyzer object
        self.assertIsInstance(analyzer1, Analyzer)

    def test_9_analyzer_jackpot(self):
        """Test jackpot calculation"""
        faces = np.array(['A', 'B', 'C', 'D', 'E', 'F'])
        die9 = Die(faces)
        game5 = Game([die9])
        game5.play(10)
        analyzer2 = Analyzer(game5)
        
        #check that the jackpot count is an integer
        self.assertIsInstance(analyzer2.jackpot(), int)
    
    def test_10_analyzer_face_counts_per_roll(self):
        """Test face counts per roll calculation"""
        faces = np.array(['A', 'B', 'C', 'D', 'E', 'F'])
        die10 = Die(faces)
        game6 = Game([die10])
        game6.play(10)
        analyzer3 = Analyzer(game6)
        
        #check that the face counts DataFrame has the correct shape
        face_counts_df = analyzer3.face_counts_per_roll()
        self.assertIsInstance(face_counts_df, pd.DataFrame)
        self.assertEqual(face_counts_df.shape[0], 10)
        self.assertEqual(face_counts_df.shape[1], 6)
    
    def test_11_analyzer_combo_count(self):
        """Test combo count calculation"""
        faces = np.array(['A', 'B', 'C', 'D', 'E', 'F'])
        die11 = Die(faces)
        game7 = Game([die11])
        game7.play(10)
        analyzer4 = Analyzer(game7)
        
        #check that the combo count DataFrame has the correct shape and has multiindex
        combo_count_df = analyzer4.combo_count()
        self.assertIsInstance(combo_count_df, pd.DataFrame)
        self.assertEqual(combo_count_df.shape[0], 10)
        self.assertIsInstance(combo_count_df.index, pd.MultiIndex)

    def test_12_analyzer_permutation(self):
        """Test permutation calculation"""
        faces = np.array(['A', 'B', 'C', 'D', 'E', 'F'])
        die12 = Die(faces)
        game8 = Game([die12])
        game8.play(10)
        analyzer5 = Analyzer(game8)
        
        #check that the permutation DataFrame has the correct shape and has multiindex
        permutation_df = analyzer5.permutation()
        self.assertIsInstance(permutation_df, pd.DataFrame)
        self.assertEqual(permutation_df.shape[0], 10)
        self.assertIsInstance(permutation_df.index, pd.MultiIndex)


if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=2, exit=False)