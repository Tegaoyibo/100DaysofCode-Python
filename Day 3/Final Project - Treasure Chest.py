print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
c1 = str(input("It's a foggy night, and you're at a cross road. Where do you want to go? Type \"left\" or \"right\""))
c1 = c1.lower()
if c1 == "right":
    print("You take the path on the right. As you traverse the path, the fog gets thicker and thicker.\nYou can no longer see what's in front of you. You must turn back")
elif c1 == "left":
    print("You take the path on the left. Though the combination of the fog and the night has greatly reduced visibility, you feel the ground beneath you get more damp and mushy.")
else:
    print("Invalid input.")

c2 = str(input("Eventually the damp and mushy path leads you to a body of water. Will you swim across or wait?"))
c2 = c2.lower()
if c2 == "swim":
    print("You attempt to swim across the body of water, but quickly realize that it is deceptively long.\nYou try your best to swim to the other side, but your stamina eventually runs low.\nYou drown.")
elif c2 == "wait":
    print("You wait before crossing the body of water. After a couple of minutes a boat emerges from the water.")
    print("You decide to take the boat across the body of water. The boat safely gets you to your destination. You see cabin in the middle of the forest.")
else:
     print("Invalid input.")

c3 = str(input("The cabin has three doors. One red. One yellow. One blue. Which door do you choose? red, yellow, or blue?"))
c3 = c3.lower()
if c3 == "red":
    print("Though you try your hardest to open the door. It does not open.\nHeat starts to arise from the door. The cabin is suddenly engulfed in flames! You lose.")
elif c3 == "blue":
    print("Though you try your hardest to open the door. It does not open.\nYou notice water seeping out from underneath the door. The cabin is suddenly flooded! You lose.")
elif c3 == "yellow":
    print("The door opens with relative ease and you find the golden treasure chest. You win!")
else:
    print("Invalid input.")