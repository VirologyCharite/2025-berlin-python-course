import marimo

__generated_with = "0.14.16"
app = marimo.App(width="medium")


@app.cell
def _():
    #count vowels in words
    def count_vowels(word):
        count_vowels = 0
        vowels_set = ("a","e","i","o","u", "A", "E", "I", "O", "U")
        for letter in word:
            if letter in vowels_set:
                count_vowels +=1
            
        return count_vowels
    
    print(count_vowels("Ilia"))

    return


if __name__ == "__main__":
    app.run()
