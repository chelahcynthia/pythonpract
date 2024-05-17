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

