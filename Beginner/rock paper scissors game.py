RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
RESET = '\033[0m'

import random
possibleactions = ["rock", "paper", "scissors"]
print(RED +"-----------------------------------------------")
print(RED +"│"+ BLUE +"Would you like to play rock, paper, scissors?"+ RED +"│")
print(RED +"│"+ BLUE +"---------------"+ BLUE +"Type "+ GREEN +"(1)"+ BLUE +" to play--------------"+ RED +"│")
print(RED +"│------------"+ BLUE +"Type "+ GREEN +"(2)"+ BLUE +" to end progam"+ RED +"-----------│")
print(RED +"│---------------------------------------------│")
option = 0
while option < 3:
    option =int(input(YELLOW +"What option would you like to choose? "))
    computeraction = random.choice(possibleactions)
    if option == 1:
        print(BLUE +"You have procceded to play the game 'rock, paper, scissors'!")
        textoption = str(input(YELLOW +"Enter either rock, paper or scissors: "))
        if textoption == computeraction:
            print(BLUE +"It's a tie!")
        elif textoption == 'rock' and computeraction == 'paper':
            print(BLUE +"Paper beats rock!")
        elif textoption == 'rock' and computeraction == 'scissors':
            print(BLUE +"Rock beat scissors!")
        elif textoption == 'scissors' and computeraction == 'rock':
            print(BLUE +"Rock beat scissors!")
        elif textoption == 'scissors' and computeraction == 'paper':
            print(BLUE +"Scissors beat paper!")
        elif textoption == 'paper' and computeraction == 'scissors':
            print(BLUE +"Scissors beats paper!")
        elif textoption == 'paper' and computeraction == 'rock':
            print(BLUE +"Paper beats rock!")
    elif option == 2:
        print(BLUE +"You have exited the program!")
        break