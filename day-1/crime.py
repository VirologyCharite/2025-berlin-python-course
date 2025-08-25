mybook = open("/data/crime-and-punishment.txt")

# word_count_dictionary will be a dictionary that will have words as its keys and counts
# as values.
word_count_dictionary = {}


for line in mybook:
    line = line.lower()
    for word in line.split():
        for unwanted_letter in ".,:()[]\"“”":
            word = word.replace(unwanted_letter, "")

        if word in word_count_dictionary:
            word_count_dictionary[word] += 1
        else:
            word_count_dictionary[word] = 1


highest_count = 0
most_frequent_word = None


for word, count in word_count_dictionary.items():
    # print(word, count)
    if count > highest_count:
        most_frequent_word = word
        highest_count = count

print(f"The most common word is {most_frequent_word!r} with count", highest_count)
