# hangman_word_guesser.py

import random


def show_instructions():
    print(
        """
    Commands:
    guess [letter]
    quit
    """
    )


def update_display_word(secret_word, display_word, guess):
    new_display_word = ""
    for i in range(len(secret_word)):
        if secret_word[i] == guess:
            new_display_word += guess
        else:
            new_display_word += display_word[i]
    return new_display_word


secret_word = "asztal"
display_word = "_" * len(secret_word)

show_instructions()

# Game loop
while True:
    print(f"\nCurrent word: {display_word}")
    command = input("> ").strip().lower()

    if command == "quit":
        print("Thanks for playing!")
        break

    elif command.startswith("guess "):
        guess = command.split(" ")[1]
        if len(guess) != 1 or not guess.isalpha():
            print("Please guess a single letter.")
        elif guess in display_word:
            print(f"You've already guessed the letter '{guess}'.")
        else:
            if guess in secret_word:
                display_word = update_display_word(secret_word, display_word, guess)
                if display_word == secret_word:
                    print(f"Congratulations! You guessed the word: {secret_word}")
                    break
            else:
                print(f"The letter '{guess}' is not in the word.")

    else:
        print(
            "Invalid command! Use 'guess [letter]' to make a guess or 'quit' to exit."
        )

print("Game over!")
