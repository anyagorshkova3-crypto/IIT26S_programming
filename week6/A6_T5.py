def readValues(file_name:str):
    file = open(file_name, 'r', encoding='utf-8')
    amount_of_strings = 0
    for s in file:
        amount_of_strings += 1
    file.seek(0)
    content = ''
    string_number = 0
    while string_number < amount_of_strings:
        row = file.readline()
        if row !='\n':
            content += row[:-1] + ';'
        string_number += 1
    file.close()
    return content
def analyseValues(values:str):
    content = values[:-1]
    numbers = content.split(';')
    count = len(numbers)
    numbers = [int(i) for i in numbers]
    total = sum(numbers)
    greatest = max(numbers)
    average = total / count
    report = f'{count};{total};{greatest};{average:.2f}'
    return f'Count;Sum;Greatest;Average\n{count};{total};{greatest};{average:.2f}\n'
def main():
    print('Program starting.')
    file_name = input('Insert filename: ')
    print('#### Number analysis - START ####')
    print(f'File "{file_name}" results:')
    values = readValues(file_name)
    print(analyseValues(values))
    print('#### Number analysis - END ####')
    print('Program ending.')
if __name__ == "__main__":
    main()