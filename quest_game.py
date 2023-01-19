
### story game ###

# Initial situation


# level 1
level1_done = False
while level1_done == False:
    print("""
in empty cave
(LOOK/SHOUT/MOVE)""")
    choice = input("")
    if choice == "LOOK":
        print("look around")
        print("use flashlight? (Y/N)")
        sub_choice = input()
        if sub_choice == "Y":
            print("exit")
            level1_done = True
        else: 
            print("cant see")
    elif choice == "SHOUT":
        print("only echo respond")
    elif choice == "MOVE":
        print("door")
        level1_done = True
    else:
        print("choose wisely")

# level 2
print("level 2")
level2_done = False
while level2_done == False:
    print("u entered another cave and saw a dwarf who diging for gold. He also saw u and aks: Are you a thief, you want my gold?! (Y/N)")
    choice = input("")
    if choice == "Y":
        print("then fight to me! (Rock-Paper-Scissors starts)")
        print("level3")
        level2_done = True
    else:
        print("then what do u want? (EXIT/LIE)")
        sub_choice2 = input("")
        if sub_choice2 == "EXIT":
            print("Dwarf help you to go outside. The end.")
            level2_done = True
        elif sub_choice2 == "LIE":
            print("when the dwarf turned away you hit him with a stone and took all the gold but you are doomed to roam this cave forever...")
            level2_done = True