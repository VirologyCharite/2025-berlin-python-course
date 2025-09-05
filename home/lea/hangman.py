import marimo

__generated_with = "0.14.16"
app = marimo.App(width="medium")


@app.cell
def _():
    # Hangman game in Python with ASCII figure + spaces + wrong-guessed letters list

    # Secret word input
    secret_word = input("Enter the secret word: ").lower()
    # To prevent the guesser from seeing it immediately
    print("\n" * 50)

    # Setup
    guessed_letters = set()
    wrong_letters = set()
    display_word = [" " if ch == " " else "_" for ch in secret_word]  # keep spaces visible
    wrong_guesses = 0

    # ASCII hangman stages
    hangman_stages = [
        """
         -----
         |   |
             |
             |
             |
             |
        =========
        """,
        """
         -----
         |   |
         O   |
             |
             |
             |
        =========
        """,
        """
         -----
         |   |
         O   |
         |   |
             |
             |
        =========
        """,
        """
         -----
         |   |
         O   |
        /|   |
             |
             |
        =========
        """,
        """
         -----
         |   |
         O   |
        /|\\  |
             |
             |
        =========
        """,
        """
         -----
         |   |
         O   |
        /|\\  |
        /    |
             |
        =========
        """,
        """
         -----
         |   |
         O   |
        /|\\  |
        / \\  |
             |
        =========
        """
    ]

    # Game loop
    while True:
        # Show current state and already-wrong letters
        print(f"\nCurrent word: {' '.join(display_word)}")
        if wrong_letters:
            print("Wrong guesses:", ", ".join(sorted(wrong_letters)))
        else:
            print("Wrong guesses: (none)")

        guess = input("Enter a letter: ").lower()

        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters or guess in wrong_letters:
            print("You already guessed that letter.")
            continue

        # Correct guess
        if guess in secret_word:
            print(f"Correct! '{guess}' is in the word.")
            for i, letter in enumerate(secret_word):
                if letter == guess:
                    display_word[i] = guess
            guessed_letters.add(guess)
        else:
            # Wrong guess
            wrong_guesses += 1
            wrong_letters.add(guess)
            print(f"Wrong! '{guess}' is not in the word.")
            print(hangman_stages[wrong_guesses])
            if wrong_guesses == len(hangman_stages) - 1:
                print(f"\nGame Over! The secret word was: {secret_word}")
                break

        # Check if word is complete (spaces are already shown)
        if "_" not in display_word:
            print(f"\nCongratulations! You guessed the word: {''.join(display_word)}")
            break
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
