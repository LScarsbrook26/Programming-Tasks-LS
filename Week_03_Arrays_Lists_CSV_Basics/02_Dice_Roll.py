"""
TASK: 02 Dice Roll

# Skills: RNG, Loops
Simulate rolling a six-sided die X number of times:
Print each roll, store all values in a list of updated totals for each number (56 ones for example):
Allow the user to print:
- Totals for each side
- average dice roll
- Counts for each of the 6 sides
- Extend (look up how to use mathplotlib and produce a bar graph for all of the statistics)

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

import random 

def dice(rolls):
    dice = [0,0,0,0,0,0]
    result = []
    total = 0
    for i in range(rolls):
        num = random.randint(1,6)
        result.append(num)
        total = total + num
        print("roll", i + 1 , "is: ", num)
        if num == 1:
            dice[0] = dice[0] + 1
            print(dice)
        elif num == 2:
            dice[1] = dice[1] + 1
            print(dice)
        elif num == 3:
            dice[2] = dice[2] + 1
            print(dice)
        elif num == 4:
            dice[3] = dice[3] + 1
            print(dice)
        elif num == 5:
            dice[4] = dice[4] + 1
            print(dice)
        else:
            dice[5] = dice[5] + 1
            print(dice)
    return dice, total

rolls = int(input("enter how many times to roll the dice: "))
cal, total = dice(rolls)
average = total / rolls 
print("which option would you like?")
print("1 - totals for each side")
print("2 - average dice roll")
print("3 - counts for each of the 6 sides")
choice = int(input("enter your choice"))
if choice == 1:
    print(cal)
elif choice == 2:
    print("average:", int(average))
else:
    print(cal[0], "ones", cal[1], "twos", cal[2], "threes", cal[3], "fours", cal[4], "fives", cal[5], "sixes")


    
    

