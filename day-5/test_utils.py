from utils import parse_dna_structure


def test_simple_example():
    dna =    "AATGTCCCTCAAAGAA"
    struct = ".[-GTCCCTCAAA-]."

    result = parse_dna_structure(dna, struct)

    assert result == {
        "rna": [
            "A",
            "AU",
            "GUCCCUCAAA",
            "GA",
            "A",
        ],
        "structure": [
            ".",
            "[-",
            "GTCCCTCAAA",
            "-]",
            ".",
        ],
    }


def test_first_example():
    dna = "AATGTCCCTCAAAGAAAAAAAAGAGGACTATTTGGGGCTA"
    struct = "...{<{{{..[---AAAAAAAAGA-----]...}}}>}.."

    result = parse_dna_structure(dna, struct)

    assert result == {
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
            "-----]",
            "...}}}>}..",
        ],
    }
