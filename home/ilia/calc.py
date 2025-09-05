import marimo

__generated_with = "0.14.16"
app = marimo.App(width="medium")


@app.function
def evaluate(fields):
    value1, operator, value2 = fields
 
    value1 = int(value1)
    value2 = int(value2)

    if operator == "+":
        return value1 + value2
    elif operator == "-":
        return value1 - value2
    else: 
        print("Sorry, I only know to do addition and subtraction.")


@app.cell
def _():
    while True:
        line = input ("Enter your command: ")
    
        if line == "q":
            print("Goodbye")
            break

        fields = line.split()
        if len(fields) == 3:
            print(evaluate(fields))
        else:
            print ("Sorry, this doesn't work. Please use 3 fields.")
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
