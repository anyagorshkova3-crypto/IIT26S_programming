'''def copy_file(source_file: str, destination_file: str):
    source = open(source_file, "r", encoding="utf-8")
    content = ""
    row = source.readline()
    while row != "":
        row = source.readline()
        content += row
    source.close()
    destination = open(destination_file, "w", encoding="utf-8")
    destination.write(content)
    destination.close()'''

def read_file(source_file: str) -> str:
    source = open(source_file, "r", encoding="utf-8")
    content = ""
    row = source.readline()
    while row != "":
        row = source.readline()
        content += row
    source.close()
    return content
def write_file(destination_file: str, content: str):
    destination = open(destination_file, "w", encoding="utf-8")
    destination.write(content)
    destination.close()
def main():
    print("Program starting.")
    print("This program can copy a file.")
    source_file = input("Insert source filename: ")
    destination_file = input("Insert destination filename: ")
    content = read_file(source_file)
    write_file(destination_file, content)
    print(f"Reading file '{source_file}' content.")
    print("File content ready in memory.")
    print(f"Writing content into file '{destination_file}'.")
    print("Copying operation complete.")
    print("Program ending.")
main()