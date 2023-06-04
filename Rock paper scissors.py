#-------------------------------------------------------------------------------
# Name:        Rock paper sciccors
# Purpose:
#
# Author:      Shahu
#
# Created:     25-05-2023
# Copyright:   (c) User 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import random
import time

play = True

uname= input("Enter your name")
print(uname, "Welcome to the Game!")

time.sleep(1)
actions= [1,2,3]

while play:
    user= int(input("Choose: Rock[1], Paper[2], Scissors[3]" ))
    comp= random.choice(actions)

    print("User chooses", user)
    print("Computer chooses", comp)

    time.sleep(2)


    if user == comp:
        print("It is a TIE!")

    elif user == 1 and comp== 2:
        print(uname, "LOST!")
    elif user == 1 and comp== 3:
        print(uname, "WON!")
    elif user == 2 and comp== 1:
        print(uname, "WON!")
    elif user == 2 and comp== 3:
        print(uname, "LOST!")
    elif user == 3 and comp== 1:
        print(uname, "LOST!")
    elif user == 3 and comp== 2:
        print(uname, "WON!")

    time.sleep(2)
    play = str(input("Play again?"))
    if play== "no":
        play= False
        print("Thank you for playing")




