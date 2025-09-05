import marimo

__generated_with = "0.14.16"
app = marimo.App(width="medium")


@app.cell
def _():
    def print_vowels_once(word):
        vowels = "aeiou"
    
        set_vowels = set()
    
        for letter in word:
            letter = letter.lower()
            if letter in vowels:
                if letter not in set_vowels:
                    set_vowels.add(letter)
                    print(letter)

    print_vowels_once("Ilia is here")
    return


if __name__ == "__main__":
    app.run()
