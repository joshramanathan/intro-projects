yesno = ["yes", "no"]
directions = ["left", "right", "forward", "backward"]
directions2 = ["into the hole", "up the tree", "continue forward"]
directions3 = ["save the creepers", "run away"]
directions4 = ["fight", "look through the chests"]
directions5 = ["potion", "key", "armor"]
directions6 = ["open the door" "look through the chests"]
name = input("What is your name, helper of the creeper kind?\n")
sword = False
potion = False
key = False
armor = False

print("Hello " + name + "! I am CreeperKid and my kingdom has been overrun by monsters. We creepers need your help!")
print("Thousands of my people have been captured by the evil monsters. Please, help me and my people!")
print("Good luck " + name + "!\n")

response = ""
while response not in yesno:
    response = input("Would you like to step into the forest?\nyes/no\n")
    if response == "yes":
        print("You head into the forest. You hear crows cawwing in the distance.\n")
    elif response == "no":
        print("You refuse CreeperKid's offer and continue on your day.")
        quit()
    else:
        print("Try again, it's literally a yes or no question\n")

response = ""
while response not in directions:
    print("To your left, you see a hungry zombie.")
    print("To your right, there is a path deeper into the forest.")
    print("There is a colossal rock wall directly in front of you.")
    print("Behind you is the forest exit.\n")
    response = input("What direction do you move?\nleft/right/forward/backward\n")
    if response == "left":
        print("The zombie eats you and you have nothing to defend yourself with. There goes your brains.")
        quit()
    elif response == "right":
        print("You head deeper into the forest.\n")
    elif response == "forward":
        print("There seems to be a big rock wall in your way.\n")
        response = ""
    elif response == "backward":
        print("You leave the forest. You will forever be remembered as the coward, " + name + ".")
        quit()
    else:
        print("Your indecisiveness makes the zombie impatient and he eats you.\n")
        quit()

response = ""
while response not in directions2:
    print("You seem to have reached a dead end in the forest path.")
    print("There is a hole in front of you that you can climb down")
    print("There is a large tree that looks easy to climb")
    print("You can also continue into the forest without a path\n")
    response = input("Where do you go now?\nInto the hole, up the tree, or continue forward?\n")
    if response == "into the hole":
        print("You fall into solid rock, breaking your leg but you can still continue.\n")
    elif response == "up the tree":
        print("You climb up the tree but you can't see anything but jungle roof.\n")
        response = ""
    elif response == "continue forward":
        print("You wander around in the forest for hours and you finally found something!")
        print("You realize you're in the same exact clearing you started in.\n")
        response = ""
    else:
        print("Just choose a direction.\n")

response = ""
while response not in directions3:
    print("You look around and see you're in a chasm full of skeletons.")
    print("Behind the skeletons, there's creepers kept in prisons.")
    print("Behind you, you see the exit to the prison.")
    print("The skeletons haven't seemed to notice you.\n")
    response = input("What do you do?\nSave the creepers or run away?\n")
    if response == "save the creepers":
        sneakFight = input("You can either try to save them by sneaking or fighting.\n")
        if sneakFight == "sneak" or sneakFight == "sneaking":
            print("You sneak past the skeletons and have no way to rescue the creepers.")
            blowUp = input("You can convince one to blow up and open the bars or try to break through.\n")
            if blowUp == "blow up" or blowUp == "blow up and open the bars" or blowUp == "convince one to blow up" or blowUp == "convince one to blow up and open the bars":
                print("A creeper steps forward and blows up the prison bars, as well as all the other creepers.")
                print("You're pretty dumb to try this, and you failed your mission.")
                quit()
            elif blowUp == "break through" or blowUp == "try to break through":
                print("You have no way of breaking through.")
                print("The skeletons notice you and kill you.")
                quit()
            else:
                print("Your indecisiveness causes the skeletons to notice and kill you.")
                quit()
        elif sneakFight == "fight" or sneakFight == "fighting":
            print("You try to fight the skeletons but you don't have a weapon.")
            print("You're pretty stupid to try this.")
            print("The skeletons shoot and kill you.")
            quit()
        else:
            print("Your indecisiveness cause the skeletons to shoot and kill you")
            quit()
    elif response == "run away":
        print("You run into the next room, hoping the skeletons didn't notice you.\n")
    else:
        print("Standing there, the skeletons notice you and shoot you.\n")
        quit()

response = ""
while response not in directions4:
    print("The next room seems to be some sort of storage room.")
    print("It's guarded by a single skeleton that hasn't seemed to notice you yet.")
    print("The skeleton is armed with a wooden sword, but you have the element of surprise.")
    print("Or you can try to sneak past and rummage through the chests for a weapon.\n")
    response = input("What should you do?\nFight or look through the chests?\n")
    if response == "fight":
        print("You take the skeleton by surprise, and take his sword. He calls for help, and evaporates into experience orbs and bones.\n")
        sword = True
        print("The other skeletons rush to kill you.")
        fightClose = input("You can either lock the door or fight the skeletons.\n")
        if fightClose == "fight" or fightClose == "fight the skeletons":
            print("You successfully take out one skeleton, but there are too many and they overwhelm you.")
            quit()
        elif fightClose == "lock" or fightClose == "lock the door":
            print("You lock the door.")
            print("You then look through the chests.\n")
        else:
            print("The skeletons rush through and kill you.")
            quit()
    elif response == "look through the chests":
        print("You sneak past and open the chests.\n")
    else:
        print("The skeleton notices you and kills you.\n")
        quit()

response = ""
while response not in directions5:
    print("You look through the chest and find three different items.")
    print("There is a potion of invisibility, a key, or iron armor.\n")
    print("Which one would you like to take?")
    response = input("Potion, key, or armor?\n")
    if response == "potion":
        print("You take the potion of invisibility with you and drink it.\n")
        potion = True
    elif response == "key":
        print("You take the key and put it in your pocket.\n")
        print("You tell the key it will be safe.")
        key = True
    elif response == "armor":
        print("You take the armor and put it on.")
        print("You feel stronger already.\n")
        armor = True
    else:
        print("You need to choose what to take.\n")

response = ""
while response not in directions6:
    print("You're stand quietly in the room.")
    print("The skeletons outside know you're there, so there's no sneaking past them.\n")
    print("Or you can rummage through the chests.")
    response = input("Would you like to open the door or look through the chests?\n")
    if response == "open the door":
        print("You open the door...\n")
        break
    elif response == "look through the chests":
        print("You look through the chests, but the other items seemed to have disappeared.\n")
        response = ""
    else:
        print("You stand there for a couple of seconds.\n")

if potion and sword:
    print("None of the skeletons notice you, as you're completely invisible.")
    print("You sneak up on each of them and kill them, as an invisible assassin.")
    print("As you kill the last one, you notice a keychain.")
    print("You rescue the creepers and you're remembered as a hero forever in the creeper kingdom.\n")
    print("\033[1;32;0mYou Won!!\n")
    quit()
elif key:
    print("You rush over to the creepers without regard for your own life.")
    print("You quickly fit the key into the prison lock and the lock clicks...")
    print("And the key falls out. You realize the key you took isn't for the prison, as there are much more than locked door.")
    print("You idiot.")
    quit()
elif armor and sword:
    print("You throw open the door confidently.")
    print("You take out a skeleton with ease, as he can't pierce your armor.")
    print("The other skeletons quickly move in and you are utterly overwhelmed, despite your strong armor.")
    quit()
elif potion and not sword:
    print("None of th skeletons notice you, as you're completely invisible.")
    print("You sneak past all of them towards the creepers.")
    print("You have no way of freeing them. You stand there until your potion wears out.")
    quit()
elif armor and not sword:
    print("You throw open the door confidently.")
    print("You run over to the creepers, but realize you still have no way of rescuing them.")
    print("You wait for your armor to wear out and end your misery.")
    quit()
else:
    print("This result shouldn't be possible.")
    print("I did a bad")
    print("Sorry")
    quit()
