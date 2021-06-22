yesno = input("Hey kids. Do you want to hear a story?\n")
if yesno == "Yes" or yesno == "yes" or yesno =="yep":
    adj1 = input("\nName an adjective\n")
    place1 = input("\nName a place\n")
    adj2 = input("\nName an adjective\n")
    mc = input("\nName a noun\n")
    mcname = input("\nName a name\n")
    verb1 = input("\nName a verb ending with -ing\n")
    place2 = input("\nName a place\n")
    bodypart1 = input("\nName a body part\n")
    noun1 = input("\nName a noun\n")
    pluralnoun1 = input("\nName a plural noun\n")
    verb2 = input("\nName a verb ending with -ing\n")
    verb3 = input("\nName a past tense verb\n")

    print("Once upon a time, in the " + adj1 + " land of " + place1 + ", there lived the " + adj2 + " " + mc + ", named " + mcname + ". One day while " + verb1 + " through the " + place2 + ", " + mcname + " scratched their " + bodypart1 + " against a nearby " + noun1 + ". Unfortunately, a group of " + pluralnoun1 + " were " + verb2 + " close by, smelling the blood. The " + pluralnoun1 + " "  + verb3 + " " + mcname + "'s blood and they died. The end!")


elif yesno == "No" or yesno == "Nope" or yesno == "nope" or yesno == "no" or yesno == "nah":
    print("Well all right, if you insist.")
else:
    print("I'm not going to ask you again because you seem incapable of answering a yes or no question")