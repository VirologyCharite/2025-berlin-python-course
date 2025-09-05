reimport marimo

__generated_with = "0.14.16"
app = marimo.App(width="medium")


app._unparsable_cell(
    r"""
    book = open(\"/data/crime-and-punishment.txt\")

    word_count = {}

    for line in book: 
        line = line.lower()
        for word in line.split():
            for unwanted_letter in \".,:;[]{}\"\"\":
                word = word.replace (unwanted_letter, \"\")
            for unwanted_word in (\"the\", \"to\", \"and\", \"had\", \"he\", \"she\", \"of\", \"by\", \"or\"):
                word = word.replace (unwanted_word, \"\")
            if word in word_count:  
                word_count[word]+= 1
        else:
            word_count[word] = 1
    print(word_count)

    highest_word_count = 10
    most_frequent_word = ()

    for word, count in word_count.items():
        if count > highest_word_count:
            most_frequent_word = word
            highest_word_count = count

    print(f\"The most common word is {most_frequent_word!r} with count\", {highest_word_count})

    $ wc -l book


    """,
    name="_"
)


if __name__ == "__main__":
    app.run()
