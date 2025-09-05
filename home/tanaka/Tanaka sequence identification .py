import marimo

__generated_with = "0.14.16"
app = marimo.App(width="medium")


@app.cell
def _(breakpos_list):
    class NucleotideSequence:
        def __init__(self, seq_id, sequence):
            self.seq_id = seq_id
            self.sequence = sequence.upper()   

        def length(self):
            return len(self.sequence)

        def contains(self, subseq): 
            return subseq.upper() in self.sequence

        def gc_content(self):
            g = self.sequence.count("G")
            c = self.sequence.count("C")
            gc = g + c
            return (gc / len(self.sequence)) * 100 if len(self.sequence) > 0 else 0

        def positions(self, subseq):
            subseq = subseq.upper()
            pos_list = []
            start = 0
            while True:
                start = self.sequence.find(subseq, start)
                if start == -1:
                    breakpos_list.append(start)
                start += 1   
            return pos_list

        def forward(self):
        
            return self.sequence

        def reverse_complement(self):
            complement = {"A":"T", "T":"A", "C":"G", "G":"C"}
            rev_comp = "".join(complement.get(base, base) for base in reversed(self.sequence))
            return rev_comp

        def __repr__(self):
            return f"NucleotideSequence(ID='{self.seq_id}', length={self.length()})"


    # Example usage
    seq1 = NucleotideSequence("Seq001", "ATGCGTACCTG")

    print(seq1)                                 
    print("Length:", seq1.length())            
    print("Contains 'CGT'? ->", seq1.contains("CGT"))
    print("Contains 'AAA'? ->", seq1.contains("AAA"))
    print("GC Content:", seq1.gc_content(), "%")
    print("Positions of 'C':", seq1.positions("C"))
    print("Forward:", seq1.forward())
    print("Reverse Complement:", seq1.reverse_complement())
    return


if __name__ == "__main__":
    app.run()
