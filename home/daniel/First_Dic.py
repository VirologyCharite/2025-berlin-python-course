import marimo

__generated_with = "0.14.16"
app = marimo.App(width="medium")


@app.cell
def _():
    mybook = open("/data/crime-and-punishment.txt")
    print(mybook)

    word_count_dictionary = {}

    for line in mybook:
        line = line.lower()
        for word in line.split():
            if word in word_count_dictionary:
                word_count_dictionary[word] += 1
            else:
                word_count_dictionary[word] = 1

    highest_count = 0
    most_frequent_word = None

    for word, count in word_count_dictionary.items():
        if count > highest_count:
            most_frequent_word = word
            highest_count = count

    print(f"The most common word is {most_frequent_word!r} with count", highest_count)


    # NEW CODE to find the longest word
    longest_word = None
    highest_length = 0

    for word in word_count_dictionary.keys():
        if len(word) > highest_length:
            longest_word = word
            highest_length = len(word)

    print(f"The longest word is {longest_word!r} with length", highest_length)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
