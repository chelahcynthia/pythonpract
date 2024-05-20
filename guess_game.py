import random

top_of_range = input("Type a number: ")

# check if num is digit
if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    
    if top_of_range <= 0:
        print('please type a number larger than 0 next time.')
        quit()
        
        
else:
    print('please type a number next time.')
    quit()
    

# create a random number and range
random_number = random.randint(0, top_of_range)
print(random_number)

# make a guess

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    # check if it is a digit
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Please type a number next time.')
        continue
    
    if user_guess == random_number:
        print("You got it!")
        break
    elif user_guess > random_number:
        print("You were above the number!")
    else:
        print("You were below the number!")