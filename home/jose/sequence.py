import marimo

__generated_with = "0.14.16"
app = marimo.App(width="medium")


@app.cell
def _():
    df1 = open("/data/sequences-1.fasta")

    sequenced_IDs = set()

    for line in df1: 
        if line.startswith(">"):
            line = line[1:].strip()
            if line in sequenced_IDs:
                print("we have seen sequenced id", line, "before")
            sequenced_IDs.add(line)

    print("Found", len (sequenced_IDs), "unique sequence IDs")

    df2 = open("/data/sequences-1.fasta")

    sequenced_IDs_2 = set()

    for line in df2: 
        if line.startswith(">"):
            line = line[1:].strip()
            if line in sequenced_IDs:
                print("we have seen sequenced id", line, "before")
            sequenced_IDs_2.add(line)

    print("Found", len (sequenced_IDs_2), "unique sequence IDs")
    return


if __name__ == "__main__":
    app.run()
