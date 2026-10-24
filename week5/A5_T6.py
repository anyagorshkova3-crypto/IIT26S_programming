def main(count):
    choice = ""
    print("Program starting.")
    while choice != "0":
        showOptions()
        choice = askChoice()
        if choice.isnumeric() == False:
            print("Unknown option!\n")
        else:
            if choice == "1":
                print(f"Current count - {count}\n")
            elif choice == "2":
                print("Count increased!\n")
                count += 1
            elif choice == "3":
                print("Cleared count!\n")
                count = 0
            elif choice != "0" and choice != "1" and choice !="2" and choice != "3":
                print("Unknown option!\n")
    else:
        print("Exiting program.")
    print()
    print("Program ending.")
def showOptions():
    print("Options:\n1 - Show count\n2 - Increase count\n3 - Reset count\n0 - Exit")
    return None
def askChoice():
    choice = input("Your choice: ")
    return choice
choice = ""
count = 0
main(count)
