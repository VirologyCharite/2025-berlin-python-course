# Some Python utilities that help us. Possibly written by non-humans.

"""Here is the prompt I used....

Write me a Python function that takes two string arguments. One is a DNA sequence and
one contains structural information.

Return a dictionary with some information that you extract from the two strings.

Here is an example of what I want. Given these two strings (the DNA and the structure,
in that order):

    AATGTCCCTCAAAGAAAAAAAAGAGGACTATTTGGGGCTA
    ...{<{{{..[---AAAAAAAAGA-----]...}}}>}..

return this dictionary:

    {
        "rna": [
            "AAUGUCCCUC",
            "AAAG",
            "AAAAAAAAGA",
            "GGACUA",
            "UUUGGGGCUA",
        ],
        "structure": [
            "...{<{{{..",
            "[---",
            "AAAAAAAAGA",
            "----]",
            "...}}}>}..",
        ]
    }

First of all, convert the DNA to RNA.

Then, break the structure into five pieces as follows:

    1. The characters up to (but not including) the left square bracket.
    2. The characters from the left square bracket up to but not including
       the first nucleotide.
    3. The characters from the first nucleotide until (and including)
       the last nucleotide.
    4. The characters after the last nucleotide up to and including
       the right square bracket.
    5. The rest of the string.

Having broken the structure string into these five pieces, break the translated DNA
string into five pieces at the same boundaries.

"""



def parse_dna_structure(dna_sequence, structure):
    """
    Parse DNA sequence and structural information into 5 segments.
    
    Args:
        dna_sequence (str): DNA sequence to convert to RNA
        structure (str): Structural annotation string
    
    Returns:
        dict: Dictionary with 'rna' and 'structure' keys, each containing 5 segments
    """
    # Convert DNA to RNA (T -> U)
    rna_sequence = dna_sequence.replace('T', 'U')
    
    # Find the positions of the square brackets
    left_bracket_pos = structure.find('[')
    right_bracket_pos = structure.find(']')
    
    if left_bracket_pos == -1 or right_bracket_pos == -1:
        raise ValueError("Structure string must contain both '[' and ']'")
    
    # Find first and last nucleotide positions within the brackets
    # Look for nucleotides (A, C, G, T, U) between the brackets
    nucleotides = set('ACGTU')
    
    first_nucleotide_pos = None
    last_nucleotide_pos = None
    
    # Find first nucleotide after left bracket
    for i in range(left_bracket_pos + 1, right_bracket_pos):
        if structure[i] in nucleotides:
            first_nucleotide_pos = i
            break
    
    # Find last nucleotide before right bracket
    for i in range(right_bracket_pos - 1, left_bracket_pos, -1):
        if structure[i] in nucleotides:
            last_nucleotide_pos = i
            break
    
    if first_nucleotide_pos is None or last_nucleotide_pos is None:
        raise ValueError("No nucleotides found between brackets in structure")
    
    # Define the 5 breakpoints
    breakpoints = [
        left_bracket_pos,           # End of segment 1
        first_nucleotide_pos,       # End of segment 2  
        last_nucleotide_pos + 1,    # End of segment 3
        right_bracket_pos + 1,      # End of segment 4
        len(structure)              # End of segment 5
    ]
    
    # Split structure into 5 segments
    structure_segments = [
        structure[0:breakpoints[0]],                           # Segment 1
        structure[breakpoints[0]:breakpoints[1]],              # Segment 2
        structure[breakpoints[1]:breakpoints[2]],              # Segment 3
        structure[breakpoints[2]:breakpoints[3]],              # Segment 4
        structure[breakpoints[3]:breakpoints[4]]               # Segment 5
    ]
    
    # Split RNA into 5 segments at the same positions
    rna_segments = [
        rna_sequence[0:breakpoints[0]],                        # Segment 1
        rna_sequence[breakpoints[0]:breakpoints[1]],           # Segment 2
        rna_sequence[breakpoints[1]:breakpoints[2]],           # Segment 3
        rna_sequence[breakpoints[2]:breakpoints[3]],           # Segment 4
        rna_sequence[breakpoints[3]:breakpoints[4]]            # Segment 5
    ]
    
    return {
        "rna": rna_segments,
        "structure": structure_segments
    }
