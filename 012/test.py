number = "9,222,222,222,222,222,222"
cleanedNumber = ''

for char in number:
    if char in '0123456789':
        cleanedNumber = cleanedNumber + char

newNumber = int(cleanedNumber)

print("Number is: {}".format(newNumber))

for state in ["one", "two", "three", "four"]:
    print("Parrot is " + state)
