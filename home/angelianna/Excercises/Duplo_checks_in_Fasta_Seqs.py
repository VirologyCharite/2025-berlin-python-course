import marimo

__generated_with = "0.14.16"
app = marimo.App(width="medium")


@app.cell
def _():
    seqs = open ("/data/sequences-2.fasta")

    seqs_seen = set ()

    for line in seqs:
        if line.startswith(">"):
            line = line[1:].strip()
            if line in seqs_seen:
               print (f"ERROR: Seq ID \033[1m{line}\033[0m seen before!")
            seqs_seen.add(line)

    print (f"Found \033[1m{len(seqs_seen)}\033[0m unique sequence IDs")
        
    return


if __name__ == "__main__":
    app.run()
