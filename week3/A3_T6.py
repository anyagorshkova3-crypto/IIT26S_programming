print("Program starting.")
print("Welcome to the unit converter program!\nFollow the menu instructions below.\n")
print("Options:\n1 - Length\n2 - Weight\n0 - Exit")
choice1 = input("Your choice: ")
print()
if choice1 == "1":
    print("Length options:\n1 - Meters to kilometers\n2 - Kilometers to meters\n0 - Exit")
    choice2 = input("Your choice: ")
    if choice2 == "1":
        meters = float(input("Insert meters: "))
        print(f'{meters} m is {round(meters / 1000, 1)} km \n')
    elif choice2 == "2":
        kilometers = float(input("Insert kilometers: "))
        print(f'{kilometers} km is {round(kilometers * 1000, 1)} m \n')
    elif choice2 == "0":
        print("Exiting... \n")
    else:
        print("Unknown option. \n")

elif choice1 == "2":
    print("Weight options:\n1 - Grams to pounds\n2 - Pounds to grams\n0 - Exit")
    choice2 = input("Your choice: ")
    if choice2 == "1":
        grams = float(input("Insert grams: "))
        print(f'{grams} g is {round(grams / 453.592, 1)} lb \n')
    elif choice2 == "2":
        pounds = float(input("Insert pounds: "))
        print(f'{pounds} lb is {round(pounds * 453.592, 1)} g \n')
    elif choice2 == "0":
        print("Exiting... \n")
    else:
        print("Unknown option. \n")
elif choice1 == "0":
    print("Exiting... \n")
else:
    print("Unknown option. \n")
print("Program ending.")

