# Global variable (usually discouraged)
# vowels = "aeiou"


def count_vowels(word):
    # I need to know the vowels

    # I need to keep track of the count

    # I need to examine every letter in the word
    # For each letter, if it's a vowel, add one to the count

    # At the end, return the total count


def count_vowels_generic_variable_names(things):
    # This function has variables with not-very-useful generic names, like "things" and
    # "thing" and "targets".
    targets = "aeiou"
    answer = 0

    for thing in things:
        if thing in targets:
            answer += 1

    return answer


# Write a function that counts the number of vowels in a word
# and returns the total count.
def count_vowels(word):
    vowels = "aeiou"
    answer = 0

    for letter in word:
        if letter in vowels:
            answer += 1

    return answer


def count_vowels_1(word):
    vowels = "aeiou"
    answer = 0
    for letter in word:
        if letter in vowels:
            answer += 1

    return answer


def count_vowels_2(word):
    answer = 0
    for letter in word:
        if letter == "a":
            answer += 1
        elif letter == "e":
            answer += 1
        elif letter == "i":
            answer += 1
        # Etc.

    return answer


def count_vowels_3(word):
    vowels = "a", "e", "i", "o", "u"
    vowels = ("a", "e", "i", "o", "u")
    vowels = ["a", "e", "i", "o", "u"]
    vowels = "aeiou"
    vowels_dict = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}

    answer = 0
    for letter in word:
        if letter in vowels:
            answer += 1
            vowels_dict[letter] += 1

    print(vowels_dict)
    return answer



def count_vowels_mind_blower(word):
    return sum(letter in "aeiou" for letter in word)


def has_any_vowels(word):
    return any(letter in "aeiou" for letter in word)


def is_all_vowels(word):
    return all(letter in "aeiou" for letter in word)



result = count_vowels_mind_blower("it is friday aaaaa")

print(result)

print(has_any_vowels("syzygy"))

print(has_any_vowels("hello"))

print(is_all_vowels("hello"))

print(is_all_vowels("i"))
