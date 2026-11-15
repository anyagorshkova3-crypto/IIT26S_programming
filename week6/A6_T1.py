'''print("Program starting.\nThis program can read a file.")
file_name = input("Insert filename: ")
print(f'#### START "{file_name}" ####')
f = open(file_name)
for s in f:
    print(s, end="")
print()
print(f'#### END "{file_name}" ####')
print("Program ending.")'''

def readFile(Filename: str) -> str:
    Content = ''
    Filehandler = open(Filename, 'r', encoding='utf-8')
    row = Filehandler.readline()
    while row != '':
        Content += row
        row = Filehandler.readline()
    Filehandler.close()
    return Content
def main():
    print("Program starting.")
    print("This program can read a file.")
    Filename = input("Insert filename: ")
    Filecontent = readFile(Filename)
    print(f'#### START "{Filename}" ####')
    print(Filecontent)
    print(f'#### END "{Filename}" ####')
    print("Program ending.")
main()