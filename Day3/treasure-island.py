print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

forest = input(
    "You walk into a dark forest and can't see anything. Would you like to start by going left or right? ").lower()

if forest == "left":
    print("You made it through the forest!")
    lake = input(
        "You keep walking and come upon a lake. Would you like to swim accross? Or wait and see what happens? ").lower()
    if lake == "wait":
        print("You notice a boat hidden behind some rocks that can take you across and decide to hop in.")
        door = input(
            "You finally make it to a large castle with a bunch of different colored doors. Which color door do you want to open? ").lower()
        if door == "blue":
            print("Eaten by beasts.\nGame over.")
        elif door == "red":
            print("Burned by fire.\nGame over.")
        elif door == "yellow":
            print("You found the treasure!")
        else:
            print("Game over.")
    else:
        print("You were mauled by some mutilated trout.\nGame over.")
else:
    print("You fell into a hole.\nGame over.")
