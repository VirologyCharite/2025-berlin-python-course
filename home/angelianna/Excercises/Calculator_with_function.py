import marimo

__generated_with = "0.14.16"
app = marimo.App(width="medium")


@app.cell
def _():
    def evaluate(fields):
        value1, operator, value2 = fields

        value1 = int(value1)
        value2 = int(value2)
        if operator == "+":
            return(value1 + value2)
        elif operator == "-":
            return(value1 - value2)
        else:
            print("Unable to run - addition, or substraction ONLY")
        
    while True:
        line = input ("Enter command: ")

        if line == "q":
            print("Goodbye")
            break

        fields = line.split()
        if len(fields) == 3:
            print(evaluate(fields))
        else:
            print("Unable to run - Use only 3 fields")
    return


if __name__ == "__main__":
    app.run()
