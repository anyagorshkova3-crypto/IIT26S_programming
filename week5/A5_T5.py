print("Program starting.")
Word = ""
def main(Word):
    print("Options:")
    print("1 - Insert word\n2 - Show current word\n3 - Show current word in reverse\n0 - Exit")
    choice = int(input("Your choice: "))
    if choice == 1:
        Word = input("Insert word: ")
    elif choice == 2:
        print(f'Current word - "{Word}"')
    elif choice == 3:
        print(f'Word reversed - "{Word[::-1]}"')
    elif choice == 0:
        print("Exiting program.")
    else:
        print("Unknown option! try again.")
    return choice, Word
choice = 1

while choice !=0:
    choice, Word = main(Word)
    print()
print("Program ending.")