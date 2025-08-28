import argparse
from examine import get_pdf_matches
from pprint import pprint


def save_matches(filename, matches):
    print(f"Saving {len(matches)} matches found on pages in {filename}.")

    assert len(filename) > 4, "Filename is too short!"
    assert filename.endswith(".pdf"), "Filename does not contain .pdf"
    assert filename.count(".pdf") == 1

    text_filename = filename.replace(".pdf", ".txt")

    with open(text_filename, "w") as file_object:
        print(f"{len(matches)} matches were found.\n", file=file_object)

        for page_number, line_match_list in matches.items():
            print(
                f"Page {page_number} has {len(line_match_list)} matches.",
                file=file_object,
            )

            for line_number, line in line_match_list:
                print(f"  Line {line_number}: {line}", file=file_object)

            print(file=file_object)



def run():
    parser = argparse.ArgumentParser(
        description="Look for a pattern in some PDF files."
    )
    parser.add_argument("pattern", help="The pattern to use")
    parser.add_argument("files", nargs="+", help="One or more filenames")

    args = parser.parse_args()

    for filename in args.files:
        matches = get_pdf_matches(filename, args.pattern)

        if matches:
            save_matches(filename, matches)
        else:
            print(f"There were no matches in {filename}.")


if __name__ == "__main__":
    run()
