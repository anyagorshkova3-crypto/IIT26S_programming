def read_file_content(source_file:str) -> str:
    source_file = open(source_file, "r", encoding="utf-8")
    amount_of_strings = 0
    for s in source_file:
        amount_of_strings += 1
    content = ""
    source_file.seek(0)
    string_number = 0
    while string_number < amount_of_strings:
        row = source_file.readline()
        if row != '\n':
            content += row[:-1] + ';'
        string_number += 1
    source_file.close()
    return content
#print(read_file_content("A6_T4_D3.txt"))
def analyze_names(file_name):
    content = read_file_content(file_name)
    amount = content.count(';')
    avg_length = (len(content) - content.count(';')) / content.count(';')
    content = content[:-1]
    names = content.split(';')
    shortest_name = len(min(names, key = len))
    longest_name = len(max(names, key = len))
    report = f'Name count - {amount}\nShortest name - {shortest_name} chars\nLongest name - {longest_name} chars\nAverage name - {avg_length:.2f} chars'
    return report

def main():
    print("Program starting.")
    print("This program analyses a list of names from a file.")
    file_name = input("Insert filename to read: ")
    print(f'Reading names from "{file_name}".')
    print("Analysing names...")
    print("Analysis complete!")
    print("#### REPORT BEGIN ####")
    print(analyze_names(file_name))
    print("#### REPORT END ####")
    print("Program ending.")
main()