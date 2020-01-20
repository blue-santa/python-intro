choice = None

while choice != '0':
    choice = input("Please enter your choice. Enter to quit.")
    if choice == '':
        break

    print("You selected {}".format(choice))
else:
    print("Thank you")
