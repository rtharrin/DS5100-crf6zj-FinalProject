import numpy as np
import pandas as pd
from itertools import combinations_with_replacement, permutations
from collections import Counter

#Die Class
class Die:
    def __init__(self,faces: np.array):
        """Initialization method, ensure that input faces is a NumPy array of distinct string/numbers.
        Defaults all weights to 1 for each face.
        """
        #first make sure faces is a NumPy array
        if type(faces) != np.ndarray:
            raise TypeError("Parameter faces must be a NumPy array")
        
              
        #Make sure the values of faces are unique
        if faces.size != np.unique(faces).size:
            raise ValueError("The values of input faces must be unique")
        
        base_weight = [1.0]*faces.size
        self.df = pd.DataFrame(index=faces, data={'Weight':base_weight})
        
    def change_weight(self,fval,weight):
        """Method to change the weight of a single side.  
        Must ensure the fval is a valid index and the weight can be cast as numeric
        Takes input fval representing the face value and weight representing the new weight.
        """
        #make sure it is a valid face name
        if fval not in self.df.index:
            raise IndexError("Your fval is not a valid face name")
        #Make sure the weight can be cast to a numeric
        try:
            float(weight)
        except ValueError :
            raise TypeError("weight must be able to be converted to a number")
            
        self.df.loc[fval,'Weight'] = float(weight)
        
    def roll_die(self,num_rolls=1):
        """Method to roll the dice, returns a list of results. 
        Takes one optional parameter, num_rolls, identifying number of rolls desired, defaults to 1 roll.
        results are not stored internally"""
        tmp = list(self.df.sample(n=num_rolls,replace=True,weights=self.df['Weight']).index)
        return tmp
    
    def show_die(self):
        """Method returning the data frame representing the die"""
        return self.df
    
#Game Class

class Game:
    """Game class expecting a list of die.  Rolls the dies numerous times and stores results in private outcome object.
    Game objects only keep results of most recent play.
    """
    
    def __init__(self,dice):
        """Initialization method, takes a list of die objects, dice."""
        self.dice=dice
    
    def play(self, num_rolls):
        """Takes the number of rolls as only parameter, num_rolls.  
        Creates/updates the private outcome object with the results"""
        result_d = dict()
        for i, die in enumerate(self.dice):
            vals = die.roll_die(num_rolls)
            result_d[i] = vals
            
        # Create a DataFrame from the dictionary of results
        self._outcome = pd.DataFrame(result_d)
        self._outcome.index.name = 'Roll_Num'
        self._outcome.columns.name = 'Die_Num'


        
    def show_outcome(self,view="wide"):
        """Method returning the result. Options include wide and narrow, default value of wide. 
        Narrow is a stacked version of the wide format with MultiIndex.
        """
        if view.upper() == "WIDE":
            return self._outcome
        elif view.upper() == "NARROW":
            # Stack the columns to create a MultiIndex with roll number and die number
            narrow_df = self._outcome.stack().reset_index()
            # Rename columns appropriately
            narrow_df.columns = ['Roll Number', 'Die Number', 'Outcome']
            # Set MultiIndex using roll number and die number
            narrow_df = narrow_df.set_index(['Roll Number', 'Die Number'])
            return narrow_df
        else:
            raise ValueError("view must be either wide or narrow")

# Analyzer Class

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
