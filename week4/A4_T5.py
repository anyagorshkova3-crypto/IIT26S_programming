print("Program starting. \n")
start=int(input("Insert starting point: "))
stop=int(input("Insert stopping point: "))
inspection=int(input("Insert inspection point: "))
print()
if start < stop and start <= inspection and stop >= inspection:
    print("First loop - inspection with break:")
    for i in range(start, stop):
        if i == inspection:
            break
        if i != stop - 1 and i != inspection-1:
            print(i, end=" ")
        else:
            print(i, end="")
    print()
    print("Second loop - inspection with continue:")
    for i in range(start, stop):
        if i == inspection:
            continue
        if i != stop - 1:
            print(i, end=" ")
        else:
            print(i, end="")
    print()
    print()
    print("Program ending.")
elif start >= stop or start >= inspection or stop <= inspection:
    if start >= stop:
        print("Starting point value must be less than the stopping point value.")
    if start > inspection or stop < inspection:
        print("Inspection value must be within the range of start and stop.")
    print()
    print("Program ending.")