def is_anagram(word1, word2):
    # Return True if the letters in word1 are identical (including the count) to the
    # letters in word2.

    return sorted(word1) == sorted(word2)


def is_anagram_using_dicts(word1, word2):
    # Return True if the letters in word1 are identical (including the count) to the
    # letters in word2. But do not sort!

    return # ???




print(is_anagram("dada", "add"))
print(is_anagram("dada", "adad"))

print(is_anagram("monday", "dynamo"))
print(is_anagram("drawer", "reward"))
