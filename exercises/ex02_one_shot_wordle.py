"""EX02 - One-Shot Wordle."""
__author__ = "730673903"

secret = "python"
guess = input(f"What is your {len(secret)}-letter guess? ")
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

index = 0
emoji = ""


# runs the code when the length matches up
if len(guess) == len(secret):
    # checks if the letter is in the right spot
    while index < len(secret):
        # if the letter is in the right spot, add a green box
        if guess[index] == secret[index]:
            emoji += GREEN_BOX
        else:
            match = False
            n = 0
            # checks if a letter appears anywhere else in the secret word
            while n < len(secret):
                if guess[index] == secret[n]:
                    match = True
                n += 1
            # if the letter appears anywhere else in the secret word, add a yellow box
            if match:
                emoji += YELLOW_BOX
            else:
                # if the letter doesn't appears anywhere else in the secret word, add a white box
                emoji += WHITE_BOX
        index += 1
    print(emoji)
    if guess == secret:
        print("Woo! You got it!")
    else:
        print("Not quite. Play again soon!")


# runs the code until the user inputs a 6 letter word
while len(guess) != len(secret):
    guess = input(f"That was not {len(secret)} letters! Try again: ")
    # runs the code when the length matches up
    if len(guess) == len(secret):
        # checks if the letter is in the right spot
        while index < len(secret):
            if guess[index] == secret[index]:
                emoji += GREEN_BOX
            else:
                match = False
                n = 0
                # checks if a letter appears anywhere else in the secret word
                while n < len(secret):
                    if guess[index] == secret[n]:
                        match = True
                    n += 1
                # if the letter appears anywhere else in the secret word, add a yellow box
                if match:
                    emoji += YELLOW_BOX
                else:
                    # if the letter doesn't appears anywhere else in the secret word, add a white box
                    emoji += WHITE_BOX
            index += 1
        print(emoji)
        if guess == secret:
            print("Woo! You got it!")
        else:
            print("Not quite. Play again soon!")