import marimo

__generated_with = "0.14.16"
app = marimo.App(width="medium")


@app.function
def reverse_complement(sequence):
    
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    result = []
    
    for base in reversed(sequence):
        if base in complement:
            result.append(complement[base])
    
    return ''.join(result)


@app.cell
def _():
    reverse_complement("ACCGT")
    return


if __name__ == "__main__":
    app.run()
