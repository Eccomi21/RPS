import random
import os
import time
def clear(): return os.system('cls')


def start():

    print("Welcome to rock, paper, scissors!")

    round = 1  # set round count to 0
    scoreH = 0  # define variable and set the score of the player to 0
    scoreC = 0  # define variable and set the score of the computer to 0

    while round <= 3:  # set number of rounds, in this case best of 3
        clear()
        print("This is round:", round)
        print("Choose your hand!:")

        # let the player choose his sign
        human = input("[1] rock, [2] paper, [3] scissors!: ")
        # let the computer choose his sign by generating a random number between 1 and 3
        n = random.randint(1, 3)

        if human.lower() == "1":
            round += 1
            print("You chose rock!")
            if n == 1:
                print("Computer chose rock! -> stalemate")
                time.sleep(2)
            elif n == 2:
                scoreC += 1
                print("Computer chose paper! -> you lost...")
                time.sleep(2)
            elif n == 3:
                scoreH += 1
                print("Computer chose scissors! -> you won!")
                time.sleep(2)

        elif human.lower() == "2":
            round += 1
            print("You chose paper!")
            if n == 1:
                scoreH += 1
                print("Computer chose rock! -> you won!")
                time.sleep(2)
            elif n == 2:
                print("Computer chose paper! -> stalemate")
                time.sleep(2)
            elif n == 3:
                scoreC += 1
                print("Computer chose scissors! -> you lost...")
                time.sleep(2)

        elif human.lower() == "3":
            round += 1
            print("You chose scissors!")
            if n == 1:
                scoreC += 1
                print("Computer chose rock! -> you lost...")
                time.sleep(2)
            elif n == 2:
                scoreH += 1
                print("Computer chose paper! -> you won!")
                time.sleep(2)
            elif n == 3:
                print("Computer chose scissors! -> stalemate")
                time.sleep(2)
        else:
            print("please choose a number")

    clear()
    print("The results 'best of 3' are:")
    print("Player:", scoreH)
    print("Computer:", scoreC)
    if scoreH > scoreC:
        print("Player won!")
    elif scoreH < scoreC:
        print("Computer won!")
    elif scoreH == scoreC:
        print("thats a stalemate")
    time.sleep(3)
    replay()


def replay():

    end = input("would you like to play again? (y/n): ")
    if end.lower() == "y":
        start()
    elif end.lower() == "n":
        exit
    else:
        print("please choose y or n")
        time.sleep(1)
        clear()
        replay()


start()