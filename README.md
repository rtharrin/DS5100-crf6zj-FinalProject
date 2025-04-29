# DS5100-crf6zj-FinalProject
Author: Ryan Harrington

# Purpose

This project consits of 3 classes to create a monte carlo simulator.  There are three classes, die, game, and analyzer. that make up the project.

# Installation and Use

## Install

You can install the project using pip-install

```
pip install 
```

## Using Die class

You can create a die class by passing it a numpy array of characters or numbers

```
import montecarlo.simulator as s

tmp =np.array(['A','B','C','D','E','F'])

die1=s.Die(tmp)

die1.showdie()
```

You can change the weight of a face using the change_weight method

```
die1.change_weight("F",3)
die1.show_die()
```

and roll the die using the roll_die method

```
die1.roll_die(3)
```

## Using the Game Class

Game class expectia a list of die objects.  Rolls the dies numerous times and stores results in private outcome object. Game objects only keep results of most recent play.

```
tmp_lst = [die1,die1]

test_game = s.Game(tmp_lst)

test_game.play(4)

test_game.show_outcome("wide")
```

show_outcome has 2 output formats, wide and narrow

```
test_game.show_outcome("narrow")
```

## Using the Analyzer Class

```
analyze_test = s.Analyzer(test_game)
analyze_test.jackpot()
```

# API Documentaion

For Die
```
Help on module simulator.dice in simulator:
NAME
    simulator.dice
CLASSES
    builtins.object
        Die
    
    class Die(builtins.object)
     |  Die(faces: <built-in function array>)
     |  
     |  Methods defined here:
     |  
     |  __init__(self, faces: <built-in function array>)
     |      Initialization method, ensure that input faces is a NumPy array of distinct string/numbers.
     |      Defaults all weights to 1 for each face.
     |  
     |  change_weight(self, fval, weight)
     |      Method to change the weight of a single side.  
     |      Must ensure the fval is a valid index and the weight can be cast as numeric
     |      Takes input fval representing the face value and weight representing the new weight.
     |  
     |  roll_die(self, num_rolls=1)
     |      Method to roll the dice, returns a list of results. 
     |      Takes one optional parameter, num_rolls, identifying number of rolls desired, defaults to 1 roll.
     |      results are not stored internally
     |  
     |  show_die(self)
     |      Method returning the data frame representing the die
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
```

For Game

```
Help on module simulator.game in simulator:

NAME
    simulator.game

CLASSES
    builtins.object
        Game
    
    class Game(builtins.object)
     |  Game(dice)
     |  
     |  Game class expecting a list of die.  Rolls the dies numerous times and stores results in private outcome object.
     |  Game objects only keep results of most recent play.
     |  
     |  Methods defined here:
     |  
     |  __init__(self, dice)
     |      Initialization method, takes a list of die objects, dice.
     |  
     |  play(self, num_rolls)
     |      Takes the number of rolls as only parameter, num_rolls.  
     |      Creates/updates the private outcome object with the results
     |  
     |  show_outcome(self, view='wide')
     |      Method returning the result. Options include wide and narrow, default value of wide. 
     |      Narrow is a stacked version of the wide format with MultiIndex.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
```

For Analyzer

```
NAME
    simulator.analyzer

CLASSES
    builtins.object
        Analyzer
    
    class Analyzer(builtins.object)
     |  Analyzer(game)
     |  
     |  A class to analyze the results of a dice game.
     |  Takes the results of a single game and computes various descriptive statistical properties about it.
     |  
     |  Methods defined here:
     |  
     |  __init__(self, game)
     |      Initialize an Analyzer with a Game object.
     |      Throws error is input, game, is not a Game object.
     |  
     |  combo_count(self)
     |      Compute the distinct combinations of faces rolled along with their counts.
     |      Returns a DataFrame with MultiIndex of distinct combinations and a column for the associated counts
     |  
     |  face_counts_per_roll(self)
     |      Compute how many times each face appears in each roll.
     |      The result is a DataFrame.
     |  
     |  jackpot(self)
     |      Compute how many times the game resulted in all faces being the same.
     |      Takes no input and returns the number of jackpots as a number.
     |  
     |  permutation_count(self)
     |      Compute the distinct permutations of faces rolled along with their counts.
     |      Permutations are order-dependent and may contain repetitions.
     |      
     |      Returns a dataframe with MultiIndex of distinct permutations and a column for the associated counts
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
```

