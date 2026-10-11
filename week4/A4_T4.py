print("Program starting. \n")
amount_of_words = 0
amount_of_characters = 0
word="q"
while word != "":
    word=input("Insert word (empty stops): ")
    if word != "":
        amount_of_words += 1
        amount_of_characters += len(word)
print()
print(f"- {amount_of_words} words")
print(f"- {amount_of_characters} characters")
print()
print("Program ending.")
