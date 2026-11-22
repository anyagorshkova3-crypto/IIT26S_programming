def collecting_integers():
    integer = 5
    integers = []
    while integer > 0:
        integer = int(input('Insert positive integer(negative stops): '))
        if integer > 0:
            integers.append(integer)
        else:
            print('Stopped collecting positive integers.')
    return integers
#print(collecting_integers())
def display_results():
    integers = collecting_integers()
    if len(integers) > 0:
        print(f'Displaying {len(integers)} integers:')
        for i in range(len(integers)):
            print(f'- Index {i} => Ordinal {i + 1} => Integer {integers[i]}')
    else:
        print('No integers to display.')
def main():
    print('Program starting.')
    print('Collect positive integers.')
    display_results()
    print('Program ending.')
main()