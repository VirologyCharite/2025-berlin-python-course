import marimo

__generated_with = "0.14.16"
app = marimo.App(width="medium")


app._unparsable_cell(
    r"""
    def print_vowel (word):
        vowels = \"AEIOUaeiou\"
        vowels_already_printed = set()
        times_letter_has_appeared =  {}
        answer = 0 

        for letter in word:
            if letter in vowels:
                answer += 1
                if letter not in vowels_already_printed:
                    print(letter, answer)
                    vowels_already_printed.add(letter)
        for answer >1:
        print


    print_vowel(\"AEIOUmeeting\")
    """,
    name="_"
)


if __name__ == "__main__":
    app.run()
