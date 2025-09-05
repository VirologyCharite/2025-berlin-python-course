import marimo

__generated_with = "0.14.16"
app = marimo.App(width="medium")


@app.cell
def _():
    #print only vowels of a given word 

    def print_vowels(word):
        vowels = "aeiouAEIOU"
        vowels_seen = set()
        all_vowels_seen = []

        x = input("all or just types?")
        if x == "types":
            for letter in word:
                if letter in vowels:
                    vowels_seen.add(letter)
            return print(f"For word \033[1m{word}\033[0m vowels seen are", vowels_seen)
        elif x == "all":
            for letter in word:
                if letter in vowels:
                    all_vowels_seen.append(letter)
            return print (f"For word \033[1m{word}\033[0m vowels seen are", all_vowels_seen)
        else:
            return print (f"Please only select between \033[1m'all'\033[0m and \033[1m'types'\033[0m in \033[1mlowercase\033[0m, you moron!")

    print_vowels(input("Provide input:"))

    return


if __name__ == "__main__":
    app.run()
