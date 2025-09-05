import marimo

__generated_with = "0.14.16"
app = marimo.App(width="medium")


@app.cell
def _(low):


    def countvowels(word):
        vowel = ("aeiou")
        count = 0
        for letter in low.word:
            if letter in vowel:
                count += 1        
        return print("There are", count, "vowels in the word", word)


    def wordswithvowels(word):
        vowel = ("aeiou")
        count = 0
        if any(letter in vowel for letter in word):
            count += 1  
        return print(count)

    countvowels (input())

    wordswithvowels (input())

    return


@app.cell
def _():
    def printvowels(word):
        for letter in word:
                if letter == "a":
                    print("a")
                elif letter == "e":
                    print("e")
                elif letter == "u":
                    print("u")
                elif letter == "i":
                    print("i")
                elif letter == "o":
                    print("o")
        return 
    printvowels (input())



    return


@app.cell
def _():
    vowelstoprint = ("")

    def printvowels(word):
        for letter in word:
            vowel = ("aeiou")
            if letter in vowel:
                printvowels.add(letter)
        return print(vowelstoprint)

    printvowels (input())



    return


@app.cell
def _():


    return


if __name__ == "__main__":
    app.run()
