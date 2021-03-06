### Rock Paper Scissors ### 

import random

# opening message
print("Let's play a game of rock paper scissors! ")       

# first player input
def rock_paper_scissors():    
    print("Chose between 'rock' 'paper' or 'scissors' and we will see who wins between us!")
    p1 = input("Your answer: ").lower().strip()

# action list to pull from
    g = ["rock", "paper", "scissors"]

# cpu input
    cpu = random.randint(0,2)
    def cpu_input(): # <<< called line 26 
        print("My answer:", g[cpu])

# game algorithm
    while not (p1 == g[0] or p1 == g[1] or p1 == g[2]): # <<< repeats input prompt until valid input is given
        p1 = input("Sorry I couldnt understand you, please type 'rock', 'paper', or 'scissors' for us to play. ").lower().strip()
        g = ["rock", "paper", "scissors"]
    else:
        cpu_input() 
        # player choses rock
        if p1 == g[0]:
            if cpu == 1:
                print("I beat you!")
            elif cpu == 2:
                print ("You beat me?!?") 
            else:
                print("Again!")
                rock_paper_scissors()
        # player choses paper
        elif p1 == g[1]:
            if cpu == 0:
                print("You beat me?!?")
            elif cpu == 2:
                print("I beat you!")
            else:
                print("Again!")
                rock_paper_scissors() 
        # player choses scissors
        elif p1 == g[2]:
            if cpu == 0:
                print("I beat you!") 
            elif cpu == 1:
                print("You beat me?!?")
            else:
                print("Again!")
                rock_paper_scissors()

    # play again promt
    def played(): 
        again = input("Would you like to play again? (Y/N)").upper().strip()
        while not (again == "Y" or again == "N"): # <<< repeats play again prompt until a valid input is given
            again = input("Sorry, I couldnt understand you. Please type 'Y' if you wish to continue or 'N' if you wish to stop.").upper().strip()    
        else:
            if again == "Y":
                print("Ok!")
                rock_paper_scissors()
            else:
                print("Okayyy... Thanks for playing! Come back soon :D")
                exit()            
    played()
rock_paper_scissors()
