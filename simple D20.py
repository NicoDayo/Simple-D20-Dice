import random
import sys

def Crit_Check(rollu):

    if rollu == 1:
        print('CRIT FAIL')
    elif rollu == 20:
        print('CRIT 20')
    
    return Crit_Check

reroll = "Y"

while reroll.lower() == "y":

    minval = 1
    maxval = 20

    print('rolling.... \n')

    print("*Vine Boom* \n")
    
    roll = (random.randint(minval, maxval))

    print(f'{roll} \n')

    Crit_Check(roll)
    print()
    reroll = input("Reroll? type y or n: ")
    if reroll.lower() == 'n':
        sys.exit()
