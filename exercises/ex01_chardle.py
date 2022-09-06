"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730488308"

guess: str = input("Enter a 5-character word: ")
if len(guess) != 5:
    print("Error: word must contain 5 characters.")
    exit()
character: str = input("Enter a single character: ")
if len(character) != 1:
    print("Error: Character must be a single character.")
    exit()
print("Searching for " + character + " in " + guess)

index1: str = guess[0]
index2: str = guess[1]
index3: str = guess[2]
index4: str = guess[3]
index5: str = guess[4]
instances: int = 0

if character == index1:
    print(character + " found at index 0")
    instances = instances + 1
if character == index2:
    print(character + " found at index 1")
    instances = instances + 1
if character == index3:
    print(character + " found at index 2")
    instances = instances + 1
if character == index4:
    print(character + " found at index 3")
    instances = instances + 1
if character == index5:
    print(character + " found at index 4")
    instances = instances + 1

if instances == 0:
    print("No instances of " + character + " found in " + guess)
if instances == 1:
    print("1 instance of " + character + " found in " + guess)
if instances == 2:
    print("2 instances of " + character + " found in " + guess)
if instances == 3:
    print("3 instances of " + character + " found in " + guess)
if instances == 4:
    print("4 instances of " + character + " found in " + guess)
if instances == 5:
    print("5 instances of " + character + " found in " + guess)