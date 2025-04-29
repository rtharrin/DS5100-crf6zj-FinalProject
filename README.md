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
tmp =np.array(['A','B','C','D','E','F'])

die1=Die(tmp)

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

# Using the Game Class

Game class expectia a list of die objects.  Rolls the dies numerous times and stores results in private outcome object. Game objects only keep results of most recent play.

```
tmp_lst = [die1,die1]

test_game = Game(tmp_lst)

test_game.play(4)

test_game.show_outcome("wide")
```

show_outcome has 2 utput formats, wide and narrow

```
test_game.show_outcome("narrow")
```

