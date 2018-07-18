from random import randint


class Dice:
    @staticmethod
    def roll(x, y):
        x = randint(x, y)
        return x


answer = ''

roll_Database = open('roll history.txt', 'a')

while answer != 'n':
    answer = input('roll again? y/n')
    dice1 = Dice.roll(1, 6)
    dice2 = Dice.roll(1, 6)
    dice_result = 'Dice 1: ' + '|' + str(dice1) + '|' + '<--------> Dice 2:' + '|' + str(dice2) + '|' + '\n'
    print(dice_result)

    roll_Database.write(dice_result)
roll_Database.close()
