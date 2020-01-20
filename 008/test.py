name = input("Name: ")
age = int(input("Age for {}: ".format(name)))
print(age)

if age >= 18:
    print("Vote")
else:
    print("Come back in {0} years".format(18 - age))

x = "false"

if x:
    print("true")

print("""
False: {0}
None: {1}
0: {2}
0.0: {3}
empty list []: {4}
empty tuple (): {5}
empty string '': {6}
empty string "": {7}
empty mapping {{}}: {8}
""".format(False, bool(None), bool(0), bool(0.0), bool([]), bool(()), bool(''), bool(""), bool({})))
