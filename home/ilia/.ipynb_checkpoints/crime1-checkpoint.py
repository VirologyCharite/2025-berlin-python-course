import marimo

__generated_with = "0.14.16"
app = marimo.App(width="medium")


@app.cell
def _():
    mybook = open("/data/crime-and-punishment.txt")
    word_count_dictionary = {}
    for line in mybook:
        line = line.lower()
        for word in line.split():
            if word in word_count_dictionary:
                word_count_dictionary[word] +=1
        else:
            word_count_dictionary[word] = 1
    highest_count = 0
    most_frequent_word = None

    for word, count in word_count_dictionary.items():
        if count > highest_count:
            most_frequent_word = word
            highest_count = count

    print("The most common word is", most_frequent_word)
    return


if __name__ == "__main__":
    app.run()
