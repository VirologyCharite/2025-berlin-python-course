f = open("/data/sequences-1.fasta")
# f = open("/data/sequences-2.fasta")

sequence_ids_seen = set()

for line in f:
    if line.startswith(">"):
        line = line[1:].strip()
        if line in sequence_ids_seen:
            # print("We have seen sequence id", line, "before")
            print(f"We have seen sequence id {line} before")

        sequence_ids_seen.add(line)

print("Found", len(sequence_ids_seen), "unique sequence ids.")
