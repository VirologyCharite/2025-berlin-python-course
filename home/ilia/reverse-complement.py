import marimo

__generated_with = "0.14.16"
app = marimo.App(width="medium")


@app.cell
def _():
    def reverse_complement(sequence):
        complement_dictionary = {"A": "T", "T": "A", "C":"G", "G":"C"}
        answer = []
        # nucleotide = "atcg"
        for nucleotide in reversed(sequence):
            print(complement_dictionary[nucleotide], end="")
            # answer.append(complement_dictionary[nucleotide])
        # return "".join(answer)

    # print(reverse_complement("ATCGGGCCTAATA"))
    reverse_complement("ATCGGGCCTAATA")

    return


if __name__ == "__main__":
    app.run()
