import numpy as np
import pandas as pd
import Die as d

class Game:
    """Game class expecting a list of die"""
    
    def __init__(self,dice):
        self.dice=dice
    
    def play(self, num_rolls):
        result = dict()
        for x in self.dice:
            key=game_test.index(x)
            vals=x.roll_die(num_rolls)
            result.update({key:vals})
            
        pd.DataFrame(result)
        