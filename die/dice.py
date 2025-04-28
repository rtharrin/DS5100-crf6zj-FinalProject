import numpy as np
import pandas as pd

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
        Takes one optional parameter, num_rolls, identifying number of rolls desired, defaults to 1 roll"""
        tmp = list(self.df.sample(n=num_rolls,replace=True,weights=self.df['Weight']).index)
        return tmp
    
    def show_die(self):
        """Method returning the data frame representing the die"""
        return self.df
    