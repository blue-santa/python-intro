available_exits = ["east", "north", "south"]

chosen_exit = ""

while chosen_exit not in available_exits:
    chosen_exit = input("Please choose an exit: ")
    if chosen_exit == "quit":
        print("Game Over")
        break

else:
    print("over") 
