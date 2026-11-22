LOWER_ALPHABETS = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
UPPER_ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
locations = {
    '0': "home",
    '1': "Galba's palace",
    '2': "Otho's palace",
    '3': "Vitellius' palace",
    '4': "Vespasian's palace"
}
def shiftCharacter(char, alphabet):
    return alphabet[alphabet.index(char) + 13]
def rot13(word):
    new_word = ''
    for i in word:
        if i.isupper():
            new_word += shiftCharacter(i, UPPER_ALPHABETS)
        elif i.islower():
            new_word += shiftCharacter(i, LOWER_ALPHABETS)
        else:
            new_word += i
    return new_word
def read_file(file_name:str):
    file = open(file_name)
    row = file.readline()
    a =[]
    while row != '':
        a.append(row)
        row = file.readline()
    file.close()
    return a
def parse_last_line():
    lines = read_file('player_progress.txt')
    last = lines[-1].strip()
    progress = last.split(';')
    return progress
def append_file(file_name:str, text:str):
    file = open(file_name, 'a', encoding='UTF-8')
    file.write(text)
    file.close()
def writeFile(file_name, content):
    file = open(file_name, 'w', encoding='UTF-8')
    file.write(content)
    file.close()
def main():
    new_message_lines = []
    progress = parse_last_line()
    print("Travel starting.")
    print(f"Currently at {locations[progress[0]]}.")
    print(f"Travelling to {locations[progress[1]]}...")
    print(f"...Arriving to the {locations[progress[1]]}.")
    plain_pass = rot13(progress[2])
    print("Passing the guard at the entrance.")
    print(f'"{plain_pass.capitalize()}!"')
    gkg_name = progress[1]+'_'+progress[2] + '.gkg'
    print("Looking for the message in the palace...")
    message_lines = read_file(gkg_name)
    print("Ah, there it is! Seems cryptic.")
    append_file('player_progress.txt', message_lines[0])
    print("[Game] Progress autosaved!")
    print("Deciphering Emperor's message...")
    for i in message_lines[1:]:
        new_message_lines.append(rot13(i))
    txt_name = progress[1] + '-' + plain_pass + '.txt'
    content = ''
    for i in new_message_lines:
        content += i
    writeFile(txt_name, content)
    print("Looks like I've got now the plain version copy of the Emperor's message.")
    print("Time to leave...")
    print("Travel ending.")
#main()
print(read_file('player_progress.txt'))