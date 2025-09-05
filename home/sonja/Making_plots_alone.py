import marimo

__generated_with = "0.14.16"
app = marimo.App(width="medium")


@app.cell
def _():
    import pandas as pd

    wine = pd.read_csv("/data/wine.csv")
    return (wine,)


@app.cell
def _(wine):
    wine
    return


@app.cell
def _():
    import matplotlib.pyplot as plt  #package for plotting
    return (plt,)


@app.cell
def _(plt, wine):
    x = wine["pH"]
    y = wine["alcohol"]

    fig, ax = plt.subplots()
    ax.scatter(x, y)  
    ax.set_xlabel("pH")
    ax.set_ylabel("alcohol")
    plt.show()


    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
