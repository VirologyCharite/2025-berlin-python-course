import marimo

__generated_with = "0.14.16"
app = marimo.App(width="medium")


@app.cell
def _():
    ###Classs: genetic sequence of an ID and string of nucleotides. 
    ## CLass has ID and sequence as atributes 
    ##Make method to see how long hte sequence is 
    ## Make a method for subsequece
    ##Make a method for a reverse sequence 



    class Sequence:
        id = set ()

    
        def __init__ (self ,id, sequence_string):
            self.id = id
            self.sequence_string = sequence_string
        def __len__ (self):
            if self.sequence_string:
                return len(self.sequence_string)
            else:
                return 0
        def reverse_complement (self):
            complementary_bases = {"A": "T", "C": "G", "G": "C", "T": "A"}
            result = []
            for nucleotide in reversed(self.sequence_string):
                pass
            result.append(complementary_bases[nucleotide])
            return "".join(result)

        def find (self, pattern): 
            if pattern in self.sequence_string: 
                print = ("I found a pattern")
            else:
                print = (" No pattern")


    seq1 = Sequence(id=1, sequence_string="ATCGATCG")
    seq2 = Sequence(id = 2, sequence_string =  "CGATTTT")

    print(f"My sequence is {seq1.sequence_string}")
    print(f"The length of the sequence is {len(seq1)} bases")
    print(f"The reverse complement is {seq1.reverse_complement()}")

    print(seq1.find("ATC"))
    print(seq2.find("TTT"))



    return


if __name__ == "__main__":
    app.run()
