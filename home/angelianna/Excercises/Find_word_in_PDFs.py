import marimo

__generated_with = "0.14.16"
app = marimo.App(width="medium")


@app.cell
def _(page_text_split, parser):
    #write a code that takes  PDF files and checks if specific words are present in there.
    #kinda alternative *NotebookLM to import PDFs and “analyze” them.
    #to read PDF files you need a library -> "pip install pypdf" in terminal (pip = python install package)

    from pypdf import PdfReader
    import argparse

    def examine_pdf(filename, pattern):
        reader = PdfReader(filename)
        page_number = 0
        matched_pages = []

        print(f"Reading {filename} ({len(reader.pages)} pages).")
    
        for page in reader.pages:
            page_number += 1
            page_text = page.extract_text().lower()
            lines = page_text_split("\n")

            line_n = 0
            for line in lines:
                line_n += 1
                if pattern in line:
                    matched_pages.append(str(page_number))
                    print(f"{line_n}:", line)

            if matched_pages:
                matched_pages_string = ",".join(matched_pages)
                print(f"{filename} has a match on page {matched_pages_string}")

    def main():
        parder = argparse.ArgumentParser(description="Look for a patter in some PDF files")
        parser.add_argument("pattern", help="The pattern to use")
        parser.add_argument("files", help="One or more file names")

        args = parser.parse_args()

        for filename in args.files:
            examine_pdf(filename, args.pattern)

    if __name__ == "__main__":
        main()

    #reader = PdfReader("example.pdf")
    #number_of_pages = len(reader.pages)
    #page = reader.pages[0]
    #text = page.extract_text()




    return


if __name__ == "__main__":
    app.run()
