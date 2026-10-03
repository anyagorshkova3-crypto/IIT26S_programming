print("Program starting. \n")
print("Options:")
print("1 - Celsius to Fahrenheit")
print('2 - Fahrenheit to Celsius')
print("0 - Exit")
choice = input("Your choice: ")
if choice =="1":
    Celsius = float(input("Insert the amount of Celsius: "))
    print(f'{Celsius} °C equals to {round((Celsius * 1.8 + 32), 1)} °F \n')
elif choice == "2":
    Fahrenheit = float(input("Insert the amount of Fahrenheit: "))
    print(f'{Fahrenheit} °F equals to {round((Fahrenheit - 32) / 1.8, 1)} °C \n')
elif choice == "0":
    print("Exiting... \n")
else:
    print("Unknown option. \n")
print("Program ending.")
