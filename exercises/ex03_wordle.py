"""The Final Wordle."""
__author__ = "730673903"


def contains_char(word: str, letter: str) -> bool: 
    """Checks if the single character is found at any index of the string."""
    assert len(letter) == 1
    n = 0
    # checks if a letter appears anywhere else in the secret word
    while n < len(word):
        if letter == word[n]:
            return True
        n += 1
    return False


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def emojified(guess: str, secret: str) -> str: 
    """Will return the green, yellow, and white emojis based on how well the guess matches up with the secret."""
    index = 0
    emoji = ""
    assert len(guess) == len(secret)
    # runs until it checks every letter and returns the emoji
    while index < len(secret):
        # if the letter matches return a green box
        if guess[index] == secret[index]:
            emoji += GREEN_BOX
        else:
            contains = contains_char(secret, guess[index])
            if contains: 
                # if the letter appears anywhere else in the secret word, return yellow box
                emoji += YELLOW_BOX
            else:
                # if the letter doesn't appear anywhere else, return white box
                emoji += WHITE_BOX
        index += 1
    return emoji
    

def input_guess(expected_length: int) -> str:
    """Keeps asking the user to enter the correct number of letters as the guess."""
    guess = input(f"Enter a {expected_length} character word: ")
    while True:
        # must be a while loop so that it continues to run until it returns something
        if len(guess) == expected_length:
            return guess
        else:
            print(f"That wasn't {expected_length} letters! Try again.")


def main() -> None: 
    """Entrypoint to the whole program."""
    # initializes all the variables
    turns = 1
    secret = "codes"
    guess = ""
    while turns <= 6 and guess != secret:
        # continues to run until the user guesses the word or tries for 6 times
        print(f"Turn {turns}/6")
        guess = input_guess(len(secret))
        emoji = emojified(guess, secret)
        print(emoji)
        if guess == secret:
            return print(f"You won in {turns}/6 turns!")
        turns += 1
    if guess != secret: 
        return print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()