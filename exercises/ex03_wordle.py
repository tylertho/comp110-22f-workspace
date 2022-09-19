"""The traditional game of Wordle."""

__author__: str = "730488308"


def main() -> None:
    """The entrypoint of the program and main game loop."""
    turns: int = 1
    win: bool = False
    secret: str = "codes"
    while turns <= 6 and win is not True:
        print(f"=== Turn {turns}/6 ===")
        guess: str = input_guess(len(secret))
        print(emojified(guess, secret))
        if guess == secret:
            print(f"You won in {turns}/6 turns!")
            win = True
        turns += 1
    if win is False:
        print("X/6 - Sorry, try again tomorrow!")


def contains_char(word: str, character: str) -> bool:
    """A function used to determine if a single character is in the first word given."""
    assert len(character) == 1
    matching_index: bool = False
    index_counter: int = 0
    while matching_index is False and index_counter < len(word):
        if word[index_counter] == character:
            matching_index = True
        else:
            index_counter += 1
    
    return matching_index


def emojified(guess: str, secret: str) -> str:
    """Returns a string of emojis testing to see correctness of guess."""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    emojis: str = ""
    counter: int = 0
    while counter < len(secret):
        if guess[counter] == secret[counter]:
            emojis += GREEN_BOX
        else:
            if contains_char(secret, guess[counter]):
                emojis += YELLOW_BOX
            else:
                emojis += WHITE_BOX
        counter += 1
    
    return emojis


def input_guess(input_number: int) -> str:
    """Receiving a guess from the user for Wordle."""
    direction: str = input(f"Enter a {input_number} character word: ")
    while len(direction) != input_number:
        direction = input(f"That wasn't {input_number} chars! Try again: ")
    return direction