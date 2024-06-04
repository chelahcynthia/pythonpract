name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input("You are on a dirt road, it has come to an end and you can go left or right.")

if answer == "left":
    answer = input("You come to a river, you can walk around it or swim across? Type walk to walk around or swim to swim around: ")
    
    if answer == 'swim':
        print("You swam across and were eaten by an alligator.")
    elif answer == 'walk':
        print("You walked for many miles, ran out of water and you lost the game.")
    else:
        print('Not a valid option. You lose.') 
        
               