import marimo

__generated_with = "0.14.16"
app = marimo.App(width="medium")


@app.cell
def _():
    def count_vowels(word): 

        count = 0
    
        for letter in word: 
            if letter == "a":
                count += 1
            elif letter == "e":
                count += 1
            elif letter == "i":
                count += 1
            elif letter == "o": 
                count += 1
            elif letter == "u":
                count += 1
        return(count)

    print(count_vowels("Dialogue"))
    print(count_vowels("meeting"))
    return


@app.cell
def _():
    def vowel_counter(word): 

        counts = 0
        vowel = "aeiou"
    
        for letter in word: 
            if letter in vowel:
                counts += 1
        return(counts)

    print(vowel_counter("Dialogue"))
    print(vowel_counter("meeting"))
    return


if __name__ == "__main__":
    app.run()
