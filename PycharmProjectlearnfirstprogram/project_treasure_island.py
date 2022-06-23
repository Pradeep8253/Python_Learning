print('''*******************************************************************************
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
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')

print("welcome to treasure Island .")
print(" your mission is to find the treasure .")
choice1 = input(' you are at a crossroad , where do you want to go ? type "right" or "left ". ').lower()
if choice1 == "left":
   choice2 = input('you\'ve  come to  a lake . there is an island in the middle of the lake . type "wait" to wait for a boat . type "swim" to swim across .').lower()
   if choice2 == "wait":
      choice3= input("you arrive at the island unharmed . there is a house with 3 doors . one red , one yellow  and one blue .which colour do you choose ?").lower()
      if choice3  =="red":
         print("it is room full of fire .Game Over ")
      elif choice3 =="yellow":
         print("you found the treasure! you win!")
      elif choice3 =="blue":
         print("you enter a room of beasts . Game Over . ")
      else:
         print("you choose a door that doesn't exits . Game Over .")
   else:
      print("you got attacked by angry troust . Game over .")
else:
   print(" you fell into a hole . Game Over .")
