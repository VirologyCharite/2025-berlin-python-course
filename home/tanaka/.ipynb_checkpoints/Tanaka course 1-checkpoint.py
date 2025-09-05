import marimo

__generated_with = "0.14.16"
app = marimo.App(width="medium")


@app.cell
def _():
    mybook = open("/data/crime-and-punishment.txt")
    return (mybook,)


@app.cell
def _(mybook):
    word_count_dictionary = {}

    # Count words in the book
    for line in mybook:  
        for word in line.split():
            # Clean unwanted characters
            for unwanted_letter in ".,:()[]":
                word = word.replace(unwanted_letter, "")
        
            # Convert to lowercase
            word = word.lower()
        
            # Count the word
            if word in word_count_dictionary:
                word_count_dictionary[word] += 1
            else:
                word_count_dictionary[word] = 1

    # Find the most frequent word
    highest_count = 0
    most_frequent_word = None

    for word, count in word_count_dictionary.items():
        if count > highest_count:
            most_frequent_word = word
            highest_count = count

    print(f"The most common word is '{most_frequent_word}' with count {highest_count}")
        
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
