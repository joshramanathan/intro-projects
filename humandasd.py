import random

def main():
    print("Guess a number between 1 and 1000.")
    rndmNumber = random.randint(1, 1000)
    found = False
    guesses = 0

    while not found:
        usGuess = int(input("Your Guess: "))

        if usGuess == rndmNumber:

            print("You got it right!")
            print("It only took you " + str(guesses) + " guesses to find the answer.")
            found = True

        elif usGuess > rndmNumber:
            print("Guess lower!")
            guesses += 1

        else:
            print("Guess higher!")
            guesses += 1

main()