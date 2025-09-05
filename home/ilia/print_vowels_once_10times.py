import marimo

__generated_with = "0.14.16"
app = marimo.App(width="medium")


@app.cell
def _():
    def print_vowels_once_at_end(word):
        vowels = "aeiou"
    
        set_vowels = set()
    
        for letter in word:
            letter = letter.lower()
            if letter in vowels:
                if letter not in set_vowels:
                    set_vowels.add(letter)
        #scores in between
        print("----".join(set_vowels))

    #10times
    for i in range (10):
        print_vowels_once_at_end("It is finally friday, not tuesday!")

    return


if __name__ == "__main__":
    app.run()
