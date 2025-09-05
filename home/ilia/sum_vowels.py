import marimo

__generated_with = "0.14.16"
app = marimo.App(width="medium")


@app.cell
def _():
    def count_vowels_mind_blower(word):
        return sum(letter in "aeiou" for letter in word)

    #klappt nicht und ich weiß auch nicht, was da los ist.
    return


if __name__ == "__main__":
    app.run()
