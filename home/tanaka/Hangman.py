import marimo

__generated_with = "0.14.16"
app = marimo.App(width="medium")


@app.cell
def _(stages):
    import random

    def hangman():
  
        # Word list
        words = ["python", "biology", "virology", "genome", "sequence", "protein"]
        secret_word = random.choice(words)
        guessed_letters = []
        tries = 6   # total wrong guesses allowed
    
        print("🎯 Welcome to Hangman!")
        print(stages[tries])   # initial empty gallows
        print("_ " * len(secret_word))  # show blanks
    
        while tries > 0:
            guess = input("Guess a letter: ").lower()

            if len(guess) != 1 or not guess.isalpha():
                print("⚠️ Please enter a single letter.")
                continue

            if guess in guessed_letters:
                print("⚠️ You already guessed that letter!")
                continue

            guessed_letters.append(guess)

            if guess in secret_word:
                print("✅ Good guess!")
            else:
                tries -= 1
                print(f"❌ Wrong guess! You have {tries} tries left.")
                print(stages[tries])  # show hangman drawing

                # Give hints as tries run out
                if tries == 3:
                    print(f"💡 Clue: The word has {len(secret_word)} letters.")
                elif tries == 2:
                    print(f"💡 Clue: The first letter is '{secret_word[0]}'.")
                elif tries == 1:
                    print(f"💡 Clue: The last letter is '{secret_word[-1]}'.")

            # Show current progress
            current_progress = [letter if letter in guessed_letters else "_" for letter in secret_word]
            print(" ".join(current_progress))

            # Check win condition
            if "_" not in current_progress:
                print("🎉 Congratulations! You guessed the word:", secret_word)
                break
        else:
            print("💀 Game over! The secret word was:", secret_word)


    # Run the game
    hangman()

    return


if __name__ == "__main__":
    app.run()
