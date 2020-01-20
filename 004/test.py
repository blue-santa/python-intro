parrot = "Norwegian Blue"

print(parrot[:7])
print(parrot[7:])
print(parrot[:])
print(parrot[-7:5])
print(parrot[-7:])
print(parrot[0:6:2])

anotherstr = "9,222,222,222,222,222"
print(anotherstr[1::4])

separators = anotherstr[1::4]

print(separators)

values = "".join(char if char not in separators else " " for char in anotherstr).split()
print([int(val) for val in values])

backwards = parrot[::-1]
print(backwards)

one = parrot[8:3:-1]
print(one)

two = parrot[8::-1]
print(two)

three = parrot[:8:-1]
