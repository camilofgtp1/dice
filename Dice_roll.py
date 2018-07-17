from random import randint
from graphics import *



class Dice:
    def roll(x, y):
        x = randint(x, y)
        return x


answer = ''

while answer != 'n':
    answer = input('roll again? y/n')
    dice1 = Dice.roll(1, 6)
    dice2 = Dice.roll(1, 6)
    print('first dice:', dice1, 'second dice', dice2)
