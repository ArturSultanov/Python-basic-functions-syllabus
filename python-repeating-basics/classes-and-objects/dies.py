from random import randint

class Die():
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        x = randint(1, self.sides)
        print(f"Score of the {self.sides}-side die roll is {x}!")
        
die_six = Die()
for i in range(10):
    die_six.roll_die()
