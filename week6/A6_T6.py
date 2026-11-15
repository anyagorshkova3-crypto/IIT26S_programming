LOWER_ALPHABETS = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
UPPER_ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"

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
def writeFile(file_name, content):
    file = open(file_name, 'w', encoding='UTF-8')
    file.write(content)
    file.close()
def main():
    print('Program starting.\n')
    print('Collecting plain text rows for ciphering.')
    words = []
    while True:
        row = input('Insert row(empty stops): ')
        if row == '':
            break
        else:
            words.append(row)
    print()
    new_words = []
    for word in words:
        new_words.append(rot13(word))
    print('#### Ciphered text ####')
    for i in new_words:
        print(i)
    print()
    print('#### Ciphered text ####')
    file_name = input('Insert filename to save: ')
    if file_name == '':
        print('File name not defined.\nAborting save operation.')
    else:
        content = ''
        for i in new_words:
            content += i + '\n'
        writeFile(file_name, content)
        print('Ciphered text saved!')
    print('Program ending.')
main()