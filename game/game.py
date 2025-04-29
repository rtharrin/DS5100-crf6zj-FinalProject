import numpy as np
import pandas as pd


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


