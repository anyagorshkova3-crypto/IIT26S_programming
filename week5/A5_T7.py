DELIMITER = ","
def main():
    print("Program starting.")
    words = collectWords()
    analyseWords(words)
    print("Program ending.")
def collectWords():
    words = ""
    word = "a"
    while word !="":
        word = input("Insert word(empty stops): ")
        if word != "":
            words += word + DELIMITER
    return words
def analyseWords(words):
    count = words.count(",")
    characters = len(words) - count
    av_length = characters / count
    print(f"- {count} Words")
    print(f"- {characters} Characters")
    print("- {:.2f} Average word length".format(av_length))
main()