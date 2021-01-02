### play a numbers guessing game against a CPU ###

import random

# global list of numbers to choose from
num = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print("Let's play a game!")

def guessing_game():
    # cpu number choice
    cpu = random.randint(0,8)
    cpuPick = num[cpu]
    #print("My number:", cpuPick) # <<< for testing purposes

    # player number choice
    print("Im thinking of a number between 1 and 9... try to guess my number: ")
    def play_game():
        play_game.counter += 1
        player = input()  

        # game algorithm 
        while player not in str(num): # <<< verifies input is valid
            print("Sorry I didnt understand you, please pick a number between 1 and 9.")
            play_game()
        else:
            pInt = int(player) # <<< converts input to int to compare guess with CPU 

            # player wins
            if cpuPick == pInt: 
                print("My number was", cpuPick)
                if play_game.counter == 1:
                    input("You got it in {} guess! ...are you a mind reader? 0_o".format(play_game.counter))
                    print("...")
                elif play_game.counter <= 3:
                    input("You got it in {} guesses! Pretty lucky huh?".format(play_game.counter))
                else:
                    print("Guessing is not your strong suit. It took you {} times to get it right... Better luck next time :P".format(play_game.counter))
                # play again prompt
                print("Would you like to play again? (Y/N) ")
                play_again()

            # player loses
            elif cpuPick + 1 == pInt:
                print("So close! Just a little lower...")
                play_game()
            elif cpuPick - 1 == pInt:
                print("So close! Just a little higher...")
                play_game()
            elif cpuPick > pInt:
                print("Too low! Try again?")
                play_game()
            elif cpuPick < pInt:
                print("Too high! Try again?")
                play_game()
            else: # <<< error for testing purposes
                print("???")

    #play again function (called line 40)
    def play_again():
        options = ["Y", "N"]
        p2 = input().upper().strip()
        while p2 not in options: # <<< verifies input is valid
            print ("Sorry, I didnt understand you, please type 'Y' if you wish to continue or 'N' if you wish to stop." )
            play_again()
        else:
            if p2 == "Y":
                print("Ok!")
                guessing_game()
            elif p2 == "N": 
                print("Okaayyy... Thanks for playing, come back soon!")
                exit()
            else: # <<< error for testing purposes
                print(p2, "???")
    play_game.counter = 0
    play_game()
guessing_game()