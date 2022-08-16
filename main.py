import random


def rollDice(sides = 20):
    print("your number is", random.randint(1, sides))


reroll = True
y = input("Would you like a roll? yes or no? ").lower()
while y not in ["no", "yes"]:
    print("Invalid Syntax, The options are yes or no.")
    y = input("Would you like a roll? yes or no?\n").lower()

if y == "yes":
    sides = int(input("How many faces would you like?\n"))
    rollDice(sides)
else:
    print("Thank you for rolling!")
    reroll = False

while reroll:
    y = input("Would you like to roll again? yes or no?\n").lower()
    while y not in ["no", "yes"]:
        print("Invalid Syntax, The options are yes or no.")
        y = input("Would you like a roll? yes or no?\n").lower()

    if y == "yes":
        sides = int(input("How many faces would you like?\n"))
        rollDice(sides)
    else:
        print("Thank you for rolling!")
        reroll = False
