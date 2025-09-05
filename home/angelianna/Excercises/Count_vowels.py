import marimo

__generated_with = "0.14.16"
app = marimo.App(width="medium")


@app.cell
def _():
    #count vowels in a string and return value of vowels

    # Fast version: return sum(letter in "aeiou" for letter in word)

    def count_vowels(word):
        vowels = "aeiouAEIOU"
        number_of_vowles = 0

        for letter in word:
            if letter in vowels:
                number_of_vowles += 1
        return print (f"For word \033[1m{word}\033[0m count is \033[1m{number_of_vowles}\033[0m")

    count_vowels(input("Provide input:"))


    return


if __name__ == "__main__":
    app.run()
