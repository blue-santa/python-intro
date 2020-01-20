number = "9,222,222,222,222,222,222"

for i in range(0, len(number)):
    print(number[i])

cleanedNumber = ''

for i in range(0, len(number)):
    if number[i] in '0123456789':
        cleanedNumber = cleanedNumber + number[i]

print()

newCleanedNumber = int(cleanedNumber)

print("The new cleaned number is {}".format(newCleanedNumber))

