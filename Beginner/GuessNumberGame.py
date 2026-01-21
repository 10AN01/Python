import random

number = random.randint(1, 20)

def playagain(): 
    Answer = int(input("Would you like to play?\n1=Yes\n2=No\n"))

    if Answer == 2:
        print("You have ended the game.")
    elif Answer == 1:
        game() 
    else:
        print("Number needs to be 1 or 2")


def game():
    pick = int(input("Guess the number from 1-50\n"))
    if pick == number:
        print("You have won!")
        playagain()
    else:
        print("Not the right number guess again")
        game()

playagain()