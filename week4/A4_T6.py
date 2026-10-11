print("Program starting.")
number_of_steps = 0
integer = int(input("Insert a positive integer: "))
print(integer, end="")
while integer != 1:
    number_of_steps += 1
    if integer % 2 == 0:
        integer = integer // 2
    else:
        integer = 3 * integer + 1
    print(f" -> {integer}", end="")
print()
print(f"Sequence had {number_of_steps} total steps.\n")
print("Program ending.")