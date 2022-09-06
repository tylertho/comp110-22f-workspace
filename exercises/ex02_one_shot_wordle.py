"""Ex02- One Short Worlde. A wordle game where the user is given unlimited attempts in finding the secret word."""

__author__: str = 730488308

secret: str = "python"
guess: str = input(f"What is your {len(secret)}-letter guess? ")

while len(guess) != len(secret):
    guess: str = input(f"That was not {len(secret)} letters! Try again: ")

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

index_counter: int = 0
result: str = ""
matching_index: bool = False
alternate_index: int = 0

while index_counter < len(secret):
    if  guess[index_counter] == secret[index_counter]:
        result: str = result + GREEN_BOX
    else:
        while matching_index == False and alternate_index < len(secret):
            if guess[index_counter] == secret[alternate_index]:
                matching_index: bool = True
            else:
                alternate_index = alternate_index + 1
        if matching_index == False:
            result = result + WHITE_BOX
        else:
            result = result + YELLOW_BOX
    index_counter = index_counter + 1
    alternate_index: int = 0
    matching_index: bool = False

print(result)

if len(guess) == len(secret):
    if guess == secret:
        print("Woo! You got it!")
    else:
        print("Not quite. Play again soon!")