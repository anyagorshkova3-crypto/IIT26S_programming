print("Program starting.")
print("Insert two integers.")
integer1 = int(input("Insert first integer: "))
integer2 = int(input("Insert second integer: "))
print("Comparing inserted integers.")
if integer1 > integer2:
    print("First integer is greater. \n")
elif integer2 > integer1:
    print("Second integer is greater. \n")
else:
    print("Integers are the same \n")
print("Adding integers together")
print(f"{integer1} + {integer2} = {integer1 + integer2} \n")
print("Checking the parity of the sum...")
if (integer1 + integer2) % 2 == 0:
    print("Sum is even.")
else:
    print("Sum is odd.")
print("Program ending.")