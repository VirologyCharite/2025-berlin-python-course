import argparse
from examine import examine_pdf


def run():
    parser = argparse.ArgumentParser(description="Look for a pattern in some PDF files.")
    parser.add_argument("pattern", help="The pattern to use")
    parser.add_argument("files", nargs="+", help="One or more filenames")

    args = parser.parse_args()

    for filename in args.files:
      examine_pdf(filename, args.pattern)


if __name__ == "__main__":
    run()
