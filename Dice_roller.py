import random as rdm
import numpy as np

def input_parse(input_string):
    
    if input_string.strip() in {"1","2","3"}:
        return int(input_string)
    else:
        print("HEY IDIOT, ENTER A VALID NUMBER FROM 1 TO 3!")
        raise SystemExit(1)
         
    
def dice_roll(num_dice):
    outcome = []
    for _ in range(num_dice):
        roll = rdm.randint(1,20)
        outcome.append(roll)
    return outcome
    
num_dice_input = input("How many D20s are being rolled? [1 - 3]")
num_dice = input_parse(num_dice_input)
outcome = dice_roll(num_dice)

print(outcome)