"""EXO1 - Chardle - A cute step toward Wordle."""
__author__ = "730673903"

word = input("Enter a 5-character word: ")
if len(word) != 5:
    print("Error: Word must contain 5 characters")
    quit()
else: 
    letter = input("Enter a single character: ")
    if len(letter) != 1:
        print("Error: Character must be a single character.")
        quit()

print("Searching for " + letter + " in " + word)
match = 0

if letter == word[0]:
    print(letter + " found at index 0")
    match += 1
if letter == word[1]:
    print(letter + " found at index 1")
    match += 1
if letter == word[2]:
    print(letter + " found at index 2")
    match += 1
if letter == word[3]:
    print(letter + " found at index 3")
    match += 1
if letter == word[4]:
    print(letter + " found at index 4")
    match += 1

if match == 1:
    print(str(match) + " instance of " + letter + " found in " + word)
if match > 1:
    print(str(match) + " instances of " + letter + " found in " + word)
if match == 0:
    print("No instances of " + letter + " found in " + word)

    