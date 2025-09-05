import marimo

__generated_with = "0.14.16"
app = marimo.App(width="medium")


@app.cell
def _():
    f = open("/data/sequences-2.fasta")
    return (f,)


@app.cell
def _(f):
    sequence_ids_seen = set()
    for line in f:
        if line.startswith (">"):
            line = line [1:].strip()
            if line in sequence_ids_seen:
                print ("We have seen sequence id", line,"before")
            sequence_ids_seen.add(line)

    print("Found", len (sequence_ids_seen),"unique sequence ids.")
    return


if __name__ == "__main__":
    app.run()
