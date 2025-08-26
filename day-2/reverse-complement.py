def reverse_complement(sequence):
    # Return the reverse complemented string of the sequence.

    # You have to reverse the sequence and then translate as follows:
    #
    # A -> T
    # C -> G
    # G -> C
    # T -> A

    complements = {
        "A": "T",
        "C": "G",
        "G": "C",
        "T": "A",
    }

    result = []

    for nucleotide in reversed(sequence):
        result.append(complements[nucleotide])

    return "".join(result)


print(reverse_complement("AGGGCT"))  # Should give you "AGCCCT"
