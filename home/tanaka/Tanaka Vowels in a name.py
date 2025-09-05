import marimo

__generated_with = "0.14.16"
app = marimo.App(width="medium")


@app.cell
def _():
    def count_vowels(word):
        vowels = "aeiou"
        count = 0 
    
        for letter in word:       
            if letter in vowels:
                count += 1
        return count

    for letter in "friday":
        print(letter)

    

    print(count_vowels("friday"))
    return


if __name__ == "__main__":
    app.run()
