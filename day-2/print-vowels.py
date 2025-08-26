# Write a function that prints the vowels in a word.
def print_vowels(word):
    vowels = "aeiou"

    print(f"The vowels in {word} are:")

    for letter in word:
        if letter in vowels:
            print(letter)


# print_vowels("friday")

# Write a function that prints the vowels in a word,
# but don't print any vowel more than once.
def print_vowels_once(word):
    vowels = "aeiou"
    already_printed = set()

    for letter in word:
        if letter in vowels:
            if letter not in already_printed:
                # We need to do two things!
                already_printed.add(letter)
                print(letter, end="")

    print()


# print_vowels_once("it is friday already!")
# print_vowels_once("xxx")

def print_vowels_once_at_end(word):
    vowels = "aeiou"
    vowels_seen = set()

    for letter in word:
        if letter in vowels:
            vowels_seen.add(letter)

    # Print the vowels we have seen in a single string.
    print("".join(vowels_seen))


# Do it 10 times.
# for i in range(10):
# print_vowels_once_at_end("It is finally friday, not tuesday!")


def print_vowels_once_lea(word):
    for vowel in "aeiou":
        if vowel in word:
            print(vowel)

# print_vowels_once_lea("It is finally friday, not tuesday!")
print_vowels_once_lea("aeiou xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
# print_vowels_once_lea("xxx a")


def print_vowels_once_optimised(word):
    vowels = "aeiou"
    vowels_seen = set()

    for letter in word:
        if letter in vowels:
            vowels_seen.add(letter)

            # If we already found all the vowels, we're done!
            if len(vowels_seen) == 5:
                break

    # Print the vowels we have seen in a single string.
    print("".join(vowels_seen))
