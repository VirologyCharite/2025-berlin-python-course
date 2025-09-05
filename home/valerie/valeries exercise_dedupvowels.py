import marimo

__generated_with = "0.14.16"
app = marimo.App(width="medium")


@app.cell
def _():
    already_printed = set()

    def printvowels(word):
        for letter in word:
            vowel = "aeiou"
            if letter in vowel:
                if letter not in already_printed:
                    already_printed.add(letter)

        print(already_printed)
    
    printvowels(input())

    return


if __name__ == "__main__":
    app.run()
