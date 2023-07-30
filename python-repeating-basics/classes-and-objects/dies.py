from random import randint

class RollingDie(): #CamelCase style
    """Class of the rolling die."""
    def __init__(self, sides=6):
        """
        Initializes attributes specific to the die.
        """
        self.sides = sides

    def roll_die(self):
        """
        Outputs information about the result of the die roll.
        """
        x = randint(1, self.sides)
        print(f"Score of the {self.sides}-side die roll is {x}!")
        
die_six = RollingDie()
for i in range(10):
    die_six.roll_die()
