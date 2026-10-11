print("Program starting.\n")
number_of_steps = 0
print("Check multiplicative persistence.")
integer = int(input("Insert an integer: "))
while integer >= 10:
    number_of_steps += 1
    product = 1
    a = [int(i) for i in str(integer)]
    for i in range(len(a) - 1):
        print(f"{a[i]} * ", end="")
        product *= a[i]
    product *= a[-1]
    print(f"{a[-1]} = {product}")
    integer = product
else:
    print("No more steps.\n")
    print(f"This program took {number_of_steps} step(s)\n")
    print("Program ending.")

