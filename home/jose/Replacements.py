import marimo

__generated_with = "0.14.16"
app = marimo.App(width="medium")


@app.cell
def _():
    #Cleans swear words
    def reverse_complement(sequence):

        complementary_bases = {"A": "T", "C": "G", "G": "C", "T": "A"}
        result = []
    
        for nucleotide in reversed(sequence):
            pass
            result.append(complementary_bases[nucleotide])
        return "-".join(result)

    reverse_complement("AGGGCT")



    return


@app.cell
def _():
    def replace_sware_words(sentence):

        replacements = {"fuck":"friggin", "shit":"sugar"}
        results = []

        for word in sentence.split(): 
                if word in replacements: 
                    results.append(replacements[word])
                else:
                    results.append(word)
        return " ".join(results)

    print(replace_sware_words("its rude to say fuck you or I dont give a shit"))
    return


if __name__ == "__main__":
    app.run()
