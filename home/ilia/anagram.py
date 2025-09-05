import marimo

__generated_with = "0.14.16"
app = marimo.App(width="medium")


@app.cell
def _():
    def is_anagram(word1, word2):
            # return true if the letters in word1 are identical (incl. the count) to the
            # letters in word2.
        return sorted(word1) == sorted(word2)

    print(is_anagram("dada", "add"))
    print(is_anagram("dynamo", "monday"))
    print(is_anagram("drawer", "reward"))
    return


if __name__ == "__main__":
    app.run()
