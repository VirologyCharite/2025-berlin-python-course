import marimo

__generated_with = "0.14.16"
app = marimo.App(width="medium")


@app.cell
def _():
    def count_vowels(word):
        return sum(letter in "aeiou" for letter in word)

    count_vowels("Friday")
    return


if __name__ == "__main__":
    app.run()
