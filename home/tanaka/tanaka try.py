import marimo

__generated_with = "0.14.16"
app = marimo.App(width="medium")


@app.cell
def _():
    #Lists and tuples

    #This is a list
    L = [4,5,6,"Hello"]

    print (L[3])
    return


@app.cell
def _():
    #This is a tuple
    T = (4,5,6,"Hello")
    #This is illegal
    # T [3] = 66
    print(T[3])

    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
