replacements = {
    "fuck": "friggin'",
    "shit": "sugar",
}


# print(replacements.get("xxx", 9999))

# try:
#     print(replacements["xxx"])
# except KeyError:
#     print("xxx is not in the dict.")


def replace_swear_words(sentence):

    result = []

    for word in sentence.split():
        result.append(replacements.get(word, word))

        # if word in replacements:
        #     result.append(replacements[word])
        # else:
        #     result.append(word)

    return " ".join(result)


print(replace_swear_words("It's rude to say fuck you or I don't give a shit !"))
