import marimo

__generated_with = "0.14.16"
app = marimo.App(width="medium")


app._unparsable_cell(
    r"""
    #write a code that takes a lot of PDF files and checks if specific words are present in there.
    #to read PDF files you need a library -> \"pip install pypdf\" in terminal (pip = python install package)

    from pypdf import PdfReader
    import argparse
    from pprint import pprint

    #function that will get the PDF files, \"read\" them and check for pattern of interest
    def get_pdf_matches(filename, pattern):
        reader = PdfReader(filename)
        page_number = 0
       # matched_pages = []

        result = {}
    
       # print(f\"Reading {filename} ({len(reader.pages)} pages).\")
    
        for page in reader.pages:
            page_number += 1
            page_text = page.extract_text().lower()
            lines = page_text_split(\"\n\")

            line_n = 0
            for line in lines:
                line_n += 1
                if pattern in line:
                   # matched_pages.append(str(page_number))
                    print(f\"{line_n}:\", line)
                    if page_number not in result:
                        result[page_number] = []
                    result[page_number].append(line_number, line)
    #####################There is a return missing here!########################
        
            if matched_pages:
                matched_pages_string = \",\".join(matched_pages)
                pprint(f\"{filename} has a match on page {matched_pages_string}\")

    #function that will save our matches in a file
    def save_matches(filename, matches):
        print(f\"Saving {len(matches)} matches found on pages in {filename}\")
    
        text_file = filename.replace(\".pdf, \".txt\")
    
        #with function guarantees that the file will be closed by Python for you!
        with open(text_filename), \"w\") as file_object:
            print(f\"Saving {len(matches)} matches found.\", file=file_object)

            for page_nuber, line_match_list in matches.items():
                print(f\"Page {page_number} has {len(line_match_list)} matches.\", file=file_object)
                for line_number, line_text in line_match_list:
                    print(f\"Line \033[1m{line_number}\033[0m: {line}.\", file=file_object)
                print(\"\")

    def main():
        parder = argparse.ArgumentParser(description=\"Look for a patter in some PDF files\")
        parser.add_argument(\"pattern\", help=\"The pattern to use\")
        parser.add_argument(\"files\", help=\"One or more file names\")

        args = parser.parse_args()

        for filename in args.files:
            matches = get_pdf_matches(filename, args.pattern)

            if matches:
                save_matches(filename, matches)
            else:
                print(\"No matches in {filename}.\")


    #This way of calling a function comes from the old days to allow other people to use your code and copy only the functions needed wo running the whole thing.
    if __name__ == \"__main__\":
        main()
    """,
    name="_"
)


if __name__ == "__main__":
    app.run()
