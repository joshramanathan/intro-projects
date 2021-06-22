import random

def main(maxNum):
    print("Guess a number between 1 and " + str(maxNum) + ".")
    rndmNumber = random.randint(1, maxNum)
    found = False
    guesses = 0
    minNum = 1
    yourGuess = maxNum/2

    while not found:


        if yourGuess == rndmNumber:

            print("You got it right.")
            print("It was " + str(rndmNumber))
            print("You took " + str(guesses) + " guesses to get it.")
            found = True

        elif yourGuess > rndmNumber:
            print(str(yourGuess))
            print("Guess lower!\n")
            maxNum = yourGuess
            yourGuess = random.randint(minNum, yourGuess)
            guesses += 1
        else:
            print(str(yourGuess))
            print("Guess higher!\n")
            minNum = yourGuess
            yourGuess = random.randint(yourGuess - 1, maxNum)
            guesses += 1

yourNumber = int(input("Your number to decode: "))
main(yourNumber)
