import random

Gamepassed = False
score = int(0)
Start_game = input("Do u want to start the number gussing game?(y/n): ")
def game():
    global score
    rand_int = random.randint(1, 10)
    guss = input("Get a number between 1 and 10: ")
    if int(guss) == rand_int:
        print("You have gussed the write number!")
        global Gamepassed
        Gamepassed = True
        

    else:
        print("Try again!")
        game()
        
        score += 1
    
    
if Start_game == "y":
    print("Welcome to the number gusser!")
    game()

else:
    print("Bye")

if Gamepassed == True:
    print("You took " + str(score + 1)+ " Tries to guss!")
else: 
    print("")
