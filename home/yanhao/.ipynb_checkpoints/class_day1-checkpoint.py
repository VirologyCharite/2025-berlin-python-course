import marimo

__generated_with = "0.14.16"
app = marimo.App()


@app.cell
def _():
    # list = open("/data/crime-and-punishment.txt")

    # count ={}

    # for line in list:
    #     line=line.lower()
    #     for word in line.split():
    #         for dele in ",./™“*”_?’!":
    #             word=word.replace(dele,"")
    #         if word in count:
    #             count[word] += 1
    #         else :
    #             count[word] = 1
    # highest_times=1

    # for word,times in count.items():
    #     if times > highest_times:
    #         answer=word
    #         highest_times=times
    # print("the most common word is",answer,", and the times is:",highest_times,".")


    return


@app.cell
def _():
    # file=open("/data/sequences-1.fasta")

    # sequnece_ids_seen=set()

    # for linee in file:
    #     if linee.startswith(">"):
    #         linee=linee[1:].strip()
    #         if linee in sequnece_ids_seen:
    #             print(linee)
    #         sequnece_ids_seen.add(linee)



    # print("found",len(sequnece_ids_seen))
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
