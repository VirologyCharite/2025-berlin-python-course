import marimo

__generated_with = "0.14.16"
app = marimo.App(width="medium")


@app.cell
def _(prin):
    f = open("/data/sequences-1.fasta")

    sequence_ids_seen = set()

    for line in f:
        if line.startswith(">"):
            line = line[1:].strip()
            if line in sequence_ids_seen:
                prin("We have seen sequence id", line, "before")
            sequence_ids_seen.add(line)

    print("Found", len(sequence_ids_seen), "unique sequence ids.")

    return


if __name__ == "__main__":
    app.run()
