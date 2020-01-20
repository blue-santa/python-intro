menu = []
menu.append(["egg", "spam", "bacon"])
menu.append(["egg", "bacon", "sausage"])


for meal in menu:
    if "spam" not in meal: 
        print(meal)
        for item in meal:
            print(item)
