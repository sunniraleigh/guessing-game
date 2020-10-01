"""A number-guessing game."""
#import random function randint
from random import randint

print("Welcome to the Guessing Game!")
name = input("What is your name? ")
randnum = randint(1, 100)
game_active = True
num_guesses = 0
roundNum = 0
bestscore = 101

#repeat forever:
#create while loop
while game_active == True:
    #ask for guess
    try:
        playernum = int(input("Guess a number: "))
        if playernum < 1 or playernum > 100:
            print("How dare you select a num out of range! Try again!")
        else:
            #check if guess is correct
            if playernum != randnum:
                num_guesses += 1
                if playernum > randnum:
                    print("Your guess is too high.")
                else:
                    print("Your guess is too low.")
            #if guess is incorrect:
                #give hint and increment number of guesses
            #if guess is correct
            else:
                num_guesses += 1
                if num_guesses < bestscore:
                    bestscore = num_guesses
                print(bestscore)
                roundNum += 1
                 #congratulate player
                print(f"Well done, {name}! You've found my number in {num_guesses} amount of valid and invalid tries!")
                askloop = True
                while askloop == True:
                    play_again = input("Do you want to play again?(y/n) ")
                    #after a round, ask player if they want to play again
                    #if player wants to play again:
                        #reset random number
                        #reset number of tries/num_guesses
                    if play_again == "y":
                        randnum = randint(1, 100)
                        num_guesses = 0
                        askloop = False
                    #if player doesn't want to play again:
                        #turn off game
                        #game_active = False
                        #Tell user how many times they played and what their best score is.
                    elif play_again == "n":
                        game_active = False
                        askloop = False
                        print(f"Your best score is {bestscore} and you played {roundNum} time(s).")
                    else:
                        print("That's not a valid response! Please enter y or n.")

    except ValueError:
        num_guesses += 1
        print("That's not a valid number. Please put an integer.")
    
    #while game is running
        #keep track of scores
        #keep track of round number