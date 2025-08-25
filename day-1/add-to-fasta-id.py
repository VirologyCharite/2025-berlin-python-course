f = open("sequences-1.fasta")

sequence_ids_seen = set()
count = 0

for line in f:
    line = line.strip()
    if line.startswith(">"):
        line = line[1:]
        if line not in sequence_ids_seen:
            count += 1
            sequence_ids_seen.add(line)
            print(f">{line} ---------> Sequence id #{count}")
    else:
        print(line)
