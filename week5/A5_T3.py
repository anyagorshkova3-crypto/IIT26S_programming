def main():
    print("Program starting.")
    UserName = askName()
    greetUser(UserName)
    print("Program ending.")
    return None
def askName():
        Pname = input("Insert name: ")
        return Pname
def greetUser(Pname):
    print(f"Hello {Pname}!")
    return None
main()