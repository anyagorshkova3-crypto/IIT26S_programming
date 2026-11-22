ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def readConfig(PFilename, PRotors):
    filehandler = open(PFilename, "r", encoding="utf-8")
    for line in filehandler:
        if line != '\n':
            PRotors.append((line.split(":")[1]).strip())
    #print(PRotors)
    filehandler.close()
    return None
def passRotor(PLetter, PRotor, PPosition):
    n = ALPHABET.index(PLetter)
    shifted = (n + PPosition) % 26
    rotor_letter = PRotor[shifted]
    shifted = (ALPHABET.index(rotor_letter) - PPosition) % 26
    return ALPHABET[shifted]
def passReflector(PLetter, PReflector):
    return PReflector[ALPHABET.index(PLetter)]
def passRotorBack(PLetter, PRotor, PPosition):
    n = ALPHABET.index(PLetter)
    shifted = (n + PPosition) % 26
    letter = ALPHABET[shifted]
    shifted = PRotor.index(letter)
    return ALPHABET[(shifted - PPosition) % 26]
def scrambleLetter(PLetter, PRotors, PReflector, PPositions):
    letter = PLetter
    letter = passRotorBack(letter, PRotors[0], PPositions[0])
    letter = passRotorBack(letter, PRotors[1], PPositions[1])
    letter = passRotorBack(letter, PRotors[2], PPositions[2])
    letter = passReflector(letter, PReflector)
    letter = passRotor(letter, PRotors[2], PPositions[2])
    letter = passRotor(letter, PRotors[1], PPositions[1])
    letter = passRotor(letter, PRotors[0], PPositions[0])
    return letter
def main():
    file_name = input("Insert config(filename): ")
    rotors = []
    readConfig(file_name, rotors)
    reflector = rotors.pop(-1)
    plugs = input("Insert plugs (y/n)?: ")
    if plugs == "n":
        print("No extra plugs inserted.")
    print("Enigma initialized.\n")
    row = input("Insert row (empty stops): ")
    while row != "":

        positions = [0, 0, 0]
        converted = ""
        for character in row:
            if character in ALPHABET:
                positions[0] += 1
                new = scrambleLetter(character, rotors, reflector,positions)
                print(f'Character "{character}" illuminated as "{new}"')
                converted += new
            else:
                print(f'Character "{character}" illuminated as "{character}"')
                converted += character
        print(f'Converted row - "{converted}".')
        print()
        row = input("Insert row (empty stops): ")
    print()
    #print(scrambleLetter("H", rotors, reflector, [1, 0, 0]))
    print("Enigma closing.")
    '''print(rotors)
    print(reflector)'''
#readConfig("iconf1.txt", [])
main()