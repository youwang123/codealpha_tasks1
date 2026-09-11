"""
Hangman Game
------------
A classic command-line Hangman game. Guess the hidden word one letter
at a time before running out of attempts!
"""

import random

WORD_LIST = [
    "python", "hangman", "programming", "developer", "keyboard",
    "computer", "algorithm", "function", "variable", "internet",
    "elephant", "giraffe", "mountain", "sandwich", "umbrella",
    "adventure", "chocolate", "dinosaur", "notebook", "penguin",
]

MAX_ATTEMPTS = 6


def choose_word():
    """Randomly select a word from the word list."""
    return random.choice(WORD_LIST)


def display_word(word, guessed_letters):
    """Show the word with unguessed letters replaced by underscores."""
    return " ".join(letter if letter in guessed_letters else "_" for letter in word)


def get_guess(guessed_letters):
    """Prompt the player for a single valid letter guess."""
    while True:
        guess = input("Guess a letter: ").lower().strip()

        if len(guess) != 1:
            print("Please enter exactly one letter.")
        elif not guess.isalpha():
            print("Please enter a valid letter.")
        elif guess in guessed_letters:
            print(f"You've already guessed '{guess}'. Try a different letter.")
        else:
            return guess


def play_game():
    """Run a single game of Hangman."""
    word = choose_word()
    guessed_letters = set()
    wrong_guesses = 0

    print("\nWelcome to Hangman!")
    print(f"The word has {len(word)} letters. You have {MAX_ATTEMPTS} wrong guesses allowed.\n")

    while wrong_guesses < MAX_ATTEMPTS:
        print("Word: " + display_word(word, guessed_letters))
        print(f"Wrong guesses: {wrong_guesses}/{MAX_ATTEMPTS}")
        if guessed_letters:
            print("Guessed letters: " + ", ".join(sorted(guessed_letters)))
        print()

        guess = get_guess(guessed_letters)
        guessed_letters.add(guess)

        if guess in word:
            print(f"Good guess! '{guess}' is in the word.\n")
            if all(letter in guessed_letters for letter in word):
                print(f"Congratulations! You guessed the word: {word.upper()}")
                return True
        else:
            wrong_guesses += 1
            print(f"Sorry, '{guess}' is not in the word.\n")

    print(f"Game over! The word was: {word.upper()}")
    return False


def main():
    """Main game loop, allowing the player to play multiple rounds."""
    wins = 0
    losses = 0

    while True:
        result = play_game()
        if result:
            wins += 1
        else:
            losses += 1

        print(f"\nScore -> Wins: {wins}  Losses: {losses}")

        again = input("\nPlay again? (y/n): ").lower().strip()
        if again != "y":
            print("Thanks for playing Hangman! Goodbye.")
            break


if __name__ == "__main__":
    main()