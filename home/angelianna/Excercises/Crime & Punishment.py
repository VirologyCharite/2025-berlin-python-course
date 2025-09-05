import marimo

__generated_with = "0.14.16"
app = marimo.App(width="medium")


@app.cell
def _():
    book = open("/data/crime-and-punishment.txt")

    #make a dictionary that contains all words with their word counts.
    words = {}

    #read the book -> open .txt reads the doc by line, so need to think of that.
    for line in book:
        #make all charecters lowercase.
        line = line.lower()
        #remove all special characters to have the same words together whether they are attached to a special character or not.
        for removable in "!,.#&()/[]_-—;:’“”?'<>1234567890\\\"":
            line = line.replace(removable, "")
        #split each line in words (separates by spaces)
        for word in line.split():
            if word in words:
                words[word] += 1
            else:
                words[word] = 1
    #print (words)

    highest_count = 0
    most_used_word = None

    for word, count in words.items():
        if count > highest_count:
            highest_count = count
            most_used_word = word

    #print the word and wordcount in bold by addint the \033[1m before and \033[0m after the bolded item.
    print (f"The word is \033[1m{most_used_word}\033[0m with a count of \033[1m{highest_count}\033[0m")
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r""" """)
    return


if __name__ == "__main__":
    app.run()
