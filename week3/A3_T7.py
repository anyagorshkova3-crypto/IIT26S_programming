print("Program starting.")
print("Testing decision structures.")
integer = int(input("Insert an integer: "))
print(f"Options:\n1 - In one multi-branched decision\n2 - In multiple independent if-statements\n0 - Exit")
option = input("Your choice: ")
if option == "1":
    print("Using one multi-branched decision structure.")
    if integer >= 400:
        integer += 44
    elif integer >= 200:
        integer += 22
    elif integer >= 100:
        integer += 11
    print(f"Result is {integer} \n")
elif option == "2":
    print("Using multiple independent if-statements structure.")
    if integer >= 400:
        integer += 44
    if integer >= 200:
        integer += 22
    if integer >= 100:
        integer += 11
    print(f"Result is {integer} \n")
elif option == "0":
    print("Exiting... \n")
else:
    print("Unknown option. \n")
print("Program ending.")