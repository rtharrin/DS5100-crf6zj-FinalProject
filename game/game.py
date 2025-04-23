import numpy as np
import pandas as pd
import Die as d

class Game:
    """Game class expecting a list of die"""
    
    def __init__(self,dice):
        self.dice=dice
    
    def play(self, num_rolls):
        """Takes the number of rolls as only parameter.  Creates/updates the outcome object with the results"""
        result_d = dict()
        for x in self.dice:
            key=game_test.index(x)
            vals=x.roll_die(num_rolls)
            result_d.update({key:vals})
            
        #Using for 1 based roll index, not needed but I should name (die_num and roll_num)
        #TODO: Make private and get rid of 1 based index
        self.outcome=pd.DataFrame(result_d, index=list(range(1,num_rolls+1)))
        
    def show_outcome(self,view="wide"):
        """Method returning the result. Options include wide and narrow, default value of wide"""
        
        if (view