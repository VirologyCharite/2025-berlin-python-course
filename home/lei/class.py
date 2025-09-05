import marimo

__generated_with = "0.14.16"
app = marimo.App(width="medium")


@app.class_definition
class Sequence:
    
    def __init__(self, id, sequence):
        self.id = id
        self.sequence = sequence
        
    def __len__(self):
        return len(self.sequence)
        
    def __str__(self):
        return f"Sequence(id='{self.id}', length={len(self.sequence)})"
    
    def __repr__(self):
        return f"Sequence(id='{self.id}', sequence='{self.sequence}')"
        
    def find(self, pattern):
        positions = []
        start = 0
        
        while True:
            pos = self.sequence.find(pattern, start)
            if pos == -1:
                break
            positions.append(pos)
            start = pos + 1
            
        return positions
    
    def count(self, pattern):
        return len(self.find(pattern))
    
    def get_subsequence(self, start, end=None):
        if end is None:
            return self.sequence[start:]
        return self.sequence[start:end]


@app.cell
def _():
    if __name__ == "__main__":
    
        dna = Sequence("seq1", "ATCGATCGATCG")
    
        print(dna)  
        print(f"Length: {len(dna)}")  
        print(f"Find 'ATC': {dna.find('ATC')}")  
        print(f"Count 'TCG': {dna.count('TCG')}")  
        print(f"Subsequence 2-8: {dna.get_subsequence(2, 8)}")  

    return


if __name__ == "__main__":
    app.run()
