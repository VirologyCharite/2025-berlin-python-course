import marimo

__generated_with = "0.14.16"
app = marimo.App(width="medium")


@app.cell
def _():
    class Sequence:
        def __init__(self, id, sequence_string):   
            self.id = id                     #saving functions
            self.sequence = sequence_string 

        def __len__(self):
            return len(self.sequence)

        def reverse_complement(self):
            comp = {"A": "T", "T": "A", "C": "G", "G": "C"}
            result = ""  # start with empty string
            for letter in reversed(self.sequence):   # letter is defined
                if letter in comp:           # if letter exists in comp dictionary
                    result += comp[letter]   # add the complement
                else:                        #but if it doesnt exist
                    result += letter         # if just keep original
            return result

        def __str__(self):                   # making it possible to print an object 
            return f"Sequence {self.id}: {self.sequence}"   #defining how to be printed


    seq = Sequence("seq1", "ATGGCATN")
    print(len(seq))                          #print only length
    print(seq.reverse_complement())          #print only reversed sequence
    print(seq)                               #print the object!

    
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
