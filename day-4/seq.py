class Sequence:

    def __init__(self, id, sequence):
        self.id = id
        self.sequence = sequence

    def __len__(self):
        return len(self.sequence)

    def gc_content(self):
        if not self.sequence:
            return 0.0

        gc_count = 0
        for nt in self.sequence.upper():
            if nt in "GC":
                gc_count += 1

        return gc_count / len(self.sequence) * 100.0

    def reverse_complement(self):
        pass

    def find(self, pattern):
        return self.sequence.find(pattern)
