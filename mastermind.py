# generate a  4color random code
# make the user guess the code
# compare the guess
# tie the game  together

import random

COLORS = ["R", "G", "B", "Y", "W", "O"]
TRIES = 10
CODE_LENGTH = 4

# fn to generate the code
def generate_code():
    code = []
    
    for _ in range(CODE_LENGTH):
        color = random.choice(COLORS)
        code.append(color)
        
    return code

# guess code
def guess_code():
    guess = input("Guess: ").upper().split("")
    