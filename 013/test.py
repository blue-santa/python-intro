meal = ["eggs", "bacon", "spam", "sausages"]

nasty_food_item = ''
for item in meal:
    if item == 'spam':
        nasty_food_item = item
        break
else:
    print("I'll have a plate of that, please")

if nasty_food_item == 'spam':
    print("Can't I have anything without spam in it?")

greeting = "Good "
greeting += "morning "

print(greeting)

greeting *= 5
print(greeting)
