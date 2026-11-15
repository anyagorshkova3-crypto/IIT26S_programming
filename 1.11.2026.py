print("=== PASSWORD MANAGER ===")
flag = True
def generate_password():
    import random
    length = int(input("Enter desired password length (minimum 8 recommended): "))
    special_characters = input("Include special characters (!@#$%^&*)? (yes/no): ")
    numbers = input("Include numbers (0-9)? (yes/no): ")
    uppercase = input("Include uppercase letters? (yes/no): ")
    print()
    characters = "abcdefghijklmnopqrstuvwxyz"
    if special_characters == "yes":
        characters += "!@#$%^&*"
    if numbers == "yes":
        characters += "0123456789"
    if uppercase == "yes":
        characters += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    is_valid = False
    while not is_valid:
        password = ""
        for i in range(length):
            password += characters[random.randint(0, len(characters)-1)]
        if (special_characters == "no" or ("!" in password or "@" in password or "#" in password or "$" in password or "%" in password or "^" in password or "&" in password or "*" in password)) \
        and (numbers == "no" or ("0" in password or "1" in password or "2" in password or "3" in password or "4" in password or "5" in password or "6" in password or "7" in password or "8" in password or "9" in password))\
        and (uppercase == "no" or ("A" in password or "B" in password or "C" in password or "D" in password or "E" in password or "F" in password or "G" in password or "H" in password or "I" in password or "J" in password or "K" in password or "L" in password or "M" in password or "N" in password or "O" in password or "P" in password or "Q" in password or "R" in password or "S" in password or "T" in password or "U" in password or "V" in password or "W" in password or "X" in password or "Y" in password or "Z" in password)):
            is_valid = True
    if is_valid:
        print(f"Generated password: {password}\n")
def check_password_strength():
    password = input("Enter password to check: ")
    print()
    length = len(password)
    has_uppercase = False
    for i in password:
        if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            has_uppercase = True
            break
    has_special = False
    for i in password:
        if i in "!@#$%^&*":
            has_special = True
            break
    print("Password check results:")
    check_length = True
    check_uppercase = True
    check_special = True
    if length < 8:
        check_length = False
        print("Password is too short (minimum 8 characters).")
    if not has_uppercase:
        check_uppercase = False
        print("No uppercase letters.")
    if not has_special:
        check_special = False
        print("No special characters.")
    if check_length == False or check_uppercase == False or check_special == False:
        print("Password is weak. It's better to change it!\n")
    else:
        print("Password is strong. Good job!\n")

while flag:
    print(f"1.Generate a strong password\n2.Check password strength\n3.Exit\n")
    choice = input("Select mode(1-3): ")
    if choice == "1":
        generate_password()
    elif choice == "2":
        check_password_strength()
    elif choice == "3":
        print("Exiting the program...")
        flag = False