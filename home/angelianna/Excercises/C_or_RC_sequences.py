import marimo

__generated_with = "0.14.16"
app = marimo.App(width="medium")


@app.cell
def _():
    #Reverse complement or complement a sequence

    def complement_or_RC(seq):
        complementarity = {"A":"T", "T":"A", "C":"G", "G":"C"}
        complement = []
        RC = []

        for base in seq:
            if base not in "ATGC":
                return print("Please provide an ATGC sequence in CAPITALS")

        x = input("C or RC?")

        for base, complementary in complementarity.items():
            if x == "C":
                for base in seq:
                    complement.append(complementarity[base])
                return print("Here's the complement", "".join(complement))

            elif x == "RC":
                for base in reversed(seq):
                    RC.append(complementarity[base])
                return print("Here's the RC", "".join(RC))

            else:
                print("Problem with the code")
        
    complement_or_RC(input("Please provide Sequence:"))

    return


if __name__ == "__main__":
    app.run()
