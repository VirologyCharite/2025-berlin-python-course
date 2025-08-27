from pypdf import PdfReader


def examine_pdf(filename, pattern):
    reader = PdfReader(filename)
    page_number = 0
    matched_pages = []

    print(f"Reading {filename} ({len(reader.pages)} pages).")

    for page in reader.pages:
        page_number += 1
        page_text = page.extract_text().lower()
        lines = page_text.split("\n")
        print(f"  Page {page_number} has {len(lines)} lines.")

        line_number = 0
        for line in lines:
            line_number += 1
            if pattern in line:
                matched_pages.append(str(page_number))
                print(f"    {line_number}: {line}")

    if matched_pages:
        matched_pages_string = ", ".join(matched_pages)
        print(f"  matches on page(s) {matched_pages_string}")


def get_pdf_matches(filename, pattern):
    reader = PdfReader(filename)
    page_number = 0
    result = {}

    for page in reader.pages:
        page_number += 1
        page_text = page.extract_text().lower()
        lines = page_text.split("\n")

        line_number = 0
        for line in lines:
            line_number += 1
            if pattern in line:
                if page_number not in result:
                    result[page_number] = []
                result[page_number].append((line_number, line))

    return result
