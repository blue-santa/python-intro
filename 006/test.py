for i in range(1, 13):
    print("No. {0:4} squared is {1:8} and cubed is {2:8}".format(i, i ** 2, i ** 3))

print()

for i in range(1, 13):
    print("No. {0:4} squared is {1:<8} and cubed is {2:<8}".format(i, i ** 2, i ** 3))

print()

print("Pi is approximately {0:12}".format(22 / 7))
print("Pi is approximately {0:12f}".format(22 / 7))
print("Pi is approximately {0:12.50f}".format(22 / 7))
print("Pi is approximately {0:52.50f}".format(22 / 7))
print("Pi is approximately {0:62.50f}".format(22 / 7))
print("Pi is approximately {0:72.50f}".format(22 / 7))
print("Pi is approximately {0:<72.54f}".format(22 / 7))

name = "bryan"

age = 24
print(age)

age_in_words = "2 years"
print(name + f" is {age} years old ")
print(type(age))

print(f"Pi is approximately {22 / 7:12.50f}")
pi = 22 / 7
print(f"Pi is approximately {pi:12.50f}")
