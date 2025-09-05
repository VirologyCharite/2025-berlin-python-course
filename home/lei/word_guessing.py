import marimo

__generated_with = "0.14.16"
app = marimo.App(width="medium")


@app.cell
def _():
    import random

    words = ["python", "computer", "game", "simple", "word", "guess", "random", "code"]

    secret_word = random.choice(words)
    guessed_letters = []
    wrong_guesses = 0
    max_wrong = 6

    print("Welcome to Word Guessing Game!")
    print(f"The word has {len(secret_word)} letters")
    print("_" * len(secret_word))

    while wrong_guesses < max_wrong:
        display = ""
        for letter in secret_word:
            if letter in guessed_letters:
                display += letter + " "
            else:
                display += "_ "
    
        print(f"\nWord: {display}")
        print(f"Wrong guesses: {wrong_guesses}/{max_wrong}")
    
        if "_" not in display:
            print("You won! The word was:", secret_word)
            break
    
        guess = input("Guess a letter: ").lower()
    
        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue
    
        guessed_letters.append(guess)
    
        if guess in secret_word:
            print("Correct!")
        else:
            print("Wrong!")
            wrong_guesses += 1

    if wrong_guesses >= max_wrong:
        print(f"Game over! The word was: {secret_word}")
    return


if __name__ == "__main__":
    app.run()
