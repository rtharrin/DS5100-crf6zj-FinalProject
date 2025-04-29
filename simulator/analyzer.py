import pandas as pd
from itertools import combinations_with_replacement, permutations
from collections import Counter
from game import Game

class Analyzer:
    """
    A class to analyze the results of a dice game.
    Takes the results of a single game and computes various descriptive statistical properties about it.
    """
    
    def __init__(self, game):
        """
        Initialize an Analyzer with a Game object.
        Throws error is input, game, is not a Game object.
        """
        if not isinstance(game, Game):
            raise ValueError("Input must be a Game object")
        self.game = game
        
    def jackpot(self):
        """ Compute how many times the game resulted in all faces being the same.
        Takes no input and returns the number of jackpots as a number.
        """
        # Get the results in wide format
        results = self.game.show_outcome("wide")
        # Check each row (roll) to see if all values in that roll are the same
        jackpots = results.apply(lambda x: x.nunique() == 1, axis=1)
        return int(jackpots.sum())
    
    def face_counts_per_roll(self):
        """
        Compute how many times each face appears in each roll.
        The result is a DataFrame.
        """
        # Get results in wide format
        results = self.game.show_outcome("wide")
        # Get unique faces from the results
        all_faces = pd.unique(results.values.ravel())
        
        # Create a new dataframe to store counts
        counts_df = pd.DataFrame(index=results.index)
        
        # For each face, count occurrences in each roll
        for face in all_faces:
            counts_df[face] = results.apply(lambda x: (x == face).sum(), axis=1)
            
        return counts_df
    
    def combo_count(self):
        """
        Compute the distinct combinations of faces rolled along with their counts.
        Returns a DataFrame with MultiIndex of distinct combinations and a column for the associated counts
        """
        # Get results in wide format
        results = self.game.show_outcome("wide")
        
        # Convert each roll to a sorted tuple (order-independent)
        combos = results.apply(lambda x: tuple(sorted(x)), axis=1)
        
        # Count occurrences of each combination
        combo_counts = Counter(combos)
        
        # Convert to dataframe with MultiIndex
        df = pd.DataFrame.from_dict(combo_counts, orient='index', columns=['Count'])
        df.index = pd.MultiIndex.from_tuples(df.index)
        
        return df
    
    def permutation_count(self):
        """
        Compute the distinct permutations of faces rolled along with their counts.
        Permutations are order-dependent and may contain repetitions.
        
        Returns a dataframe with MultiIndex of distinct permutations and a column for the associated counts
        """
        # Get results in wide format
        results = self.game.show_outcome("wide")
        
        # Convert each roll to a tuple (maintaining order)
        perms = results.apply(lambda x: tuple(x), axis=1)
        
        # Count occurrences of each permutation
        perm_counts = Counter(perms)
        
        # Convert to dataframe with MultiIndex
        df = pd.DataFrame.from_dict(perm_counts, orient='index', columns=['Count'])
        df.index = pd.MultiIndex.from_tuples(df.index)
        
        return df
