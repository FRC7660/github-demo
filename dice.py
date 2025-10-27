#!/bin/env python 

import random

permission = input("yes or no. Do you want to roll the dice? If 5, you win. ")

if permission == "yes":
    dice = random.randrange(1,6)
    print(dice)

if dice ==5:
    print("YOU WON !!!")
else:
    print("you lost :(")

if dice ==6:
    print("YOU ALOMST WON ^_^")