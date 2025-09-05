import marimo

__generated_with = "0.14.16"
app = marimo.App(width="medium")


@app.cell
def _():
    import pandas as pd
    return (pd,)


@app.cell
def _(pd):
    wine = pd.read_csv("/data/wine.csv")
    return (wine,)


@app.cell
def _(wine):
    wine

    return


if __name__ == "__main__":
    app.run()
