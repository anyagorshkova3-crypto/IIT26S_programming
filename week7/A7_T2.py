def collecting_integers():
    integers = input('Insert comma separated integers: ')
    return integers
def analysing_integers():
    integers = collecting_integers().split(',')
    valid = []
    for i in range(len(integers)):
        try:
            valid.append(int(integers[i]))
        except ValueError:
            print(f"Invalid value '{integers[i]}' detected.")
    return valid
def sum_parity():
    integers = analysing_integers()
    valid_sum = 0
    parity = 'odd'
    for i in integers:
        valid_sum += int(i)
    if valid_sum % 2 == 0:
        parity = 'even'
    if len(integers) > 0:
        print(f'There are {len(integers)} integers in the list.')
        print(f"Sum of the integers is {valid_sum} and it's {parity}")
    else:
        print("No values to analyse.")
def main():
    print('Program starting.')
    sum_parity()
    print("Program ending.")
main()