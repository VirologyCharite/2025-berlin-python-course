mybook = open("/data/crime-and-punishment.txt")

# word_count_dictionary will be a dictionary that will have words as its keys and counts
# as values.
word_count_dictionary = {}


for line in mybook:
    for word in line.split():
        if word in word_count_dictionary:
            # Get the current count for this word.
            current_count = word_count_dictionary[word]
            # print("The word", word, "is already in the dictionary, with count", current_count)

            # Add one to it.
            new_count = current_count + 1

            # Put the new value into the dictionary.
            word_count_dictionary[word] = new_count
            # print("  Updated to new count", new_count)
        else:
            word_count_dictionary[word] = 1
