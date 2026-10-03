print("Program starting.")
print("This is a program with simple menu, where you can choose which operation the program performs")
Name = input("Before the menu, please insert your name: ")
print()
print("Options:")
print("1 - Print welcome message")
print("0 - Exit")
choice = input("Your choice: ")
if choice == '1':
    print(f"Welcome {Name}! \n")
elif choice == '0':
    print("Exiting... \n")
else:
    print("Unknown option. \n")
print("Program ending.")