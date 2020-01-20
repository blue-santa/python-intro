parrot = "Norwegian Blue"

letter = input("Enter a character: ")

if letter not in parrot:
    print("Don't need that letter")
else:
    print("Give me a {}".format(letter))
