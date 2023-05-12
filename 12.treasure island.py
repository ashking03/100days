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

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
a = input("You're at the ship. Would you like to board or not (Left for yes, right for no):")
b = a.lower()
if b == 'left':
  c = input("Yay! You've reached the island. As you get down from the ship and walk further into the island you arrive infront of a huge castle. You see that the bridge leading into the castle is in pieces. Would you like to swim across or wait? (swim/wait):")
  d = c.lower()
  if d == 'wait':
    e = input("After looking for a few minutes you find a small boat with 2 oars hidden behind a bush. You row acorss the pond and enter the castle. It's beautiful inside. You can see the hallways lined by richly coloured wallpaper with intricate designs. You follow the map further into the castle and reach the tomb where the king and queen are buried. You look up and see three doors behind them. Your treasure lies behind one of those doors. You only get one choice. But be warned if you choose the wrong door, you die (red/blue/yellow):")
    f = e.lower()
    if f == 'yellow':
      print("Congragulations. You have won the treasure of Great King Nikolai Starkov. You are now the heir to his fortune.")
    elif f == 'red':
      print("As you open the door and enter inside a bomb goes off and youre blown to pieces. Better luck next time :(")
    elif f == 'blue':
      print("as you step inside the room the door closes behind you. You continue walking to a stone statue in the middle but as soon as you step infront of the statue the room starts to flood. You drown to your death. Better luck next time :(")
    else :
      print("Invalid input")
  else:
    print("Oh no, you have fallen into a pond with a type of poisonous weed. Your skin is bubbling with red boils and you're dying. Game over. Better luck next time :(")
else:
  print("Game over. You were attacked by bandits as you didn't board the ship. Game Over. Better luck next time :(")
