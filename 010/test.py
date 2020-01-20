name = input("Provide a name: ")
age = int(input("Provide an age: "))

if age >= 18 and age < 31:
    print("welcome to the party, {0}".format(name))
else:
    print("Sorry, you're not the right age")
