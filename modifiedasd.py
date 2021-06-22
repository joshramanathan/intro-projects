from random import randint
intput = input("Enter any string of numbers.\n")
found = False
guessNum = 0
minNum = len(str(10**(int(intput)-1)))
maxNum = len(str(10**(int(intput))))

def random(n):
    rangeStart = 10**(n-1)
    rangeEnd = (10**n)
    return randint(rangeStart, rangeEnd)

guess = random(len(str(intput)))

while not found:
    if guess == int(intput):
        print("I found the number!")
        print("It is " + intput + "!")
        print("I took " + str(guessNum) + " guesses to get it.")
        found = True
    elif guess > int(intput):
        print(str(guess))
        guess = random(len(str(intput)))
        guessNum += 1
    else:
        print(str(guess))
        guess = random(len(str(intput)))
        guessNum += 1