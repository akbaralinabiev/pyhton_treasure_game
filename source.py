

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')


print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

left = input("Your first mission is to find the decent way to treasure. Which direction will you choose, left or right: ")

if left == "left":
    next_mission = input("Boom! You took the next step. There is a lake in front of you, will you wait a boat to get to the other side of the lake or you swimm to there ? Type wait or swimm ")
    if (next_mission == "swimm") or (next_mission == "wait"):
        last_step = input("Great, that's the last step before you can reach the treasure, you have three doors in front of you: yellow, red and blue, guess and type the right door to get treasure ")
        if last_step == "red":
            print("You win!")
        elif (last_step == "yellow") or (last_step == "blue"):
            print("Sorry, you can't continue, this is a wrong door. Game is over.")
        else:
            print("Please type: red, yellow or blue")
elif left == "right":
    print("Sorry, this is wrong directoin, Game is over.")

else:
    print("Please type: left or right")

