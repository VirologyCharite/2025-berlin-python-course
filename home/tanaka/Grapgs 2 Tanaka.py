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


@app.cell
def _():
    import matplotlib.pyplot as plt
    return (plt,)


@app.cell
def _(plt, wine):
    plt.scatter(wine["alcohol"], wine["quality"])
    plt.xlabel("Alcohol")
    plt.ylabel("Quality")
    plt.title("Alcohol vs Quality")
    plt.show()

    return


@app.cell
def _(plt, wine):
    wine.boxplot(column="alcohol")
    plt.title("Boxplot of Alcohol")
    plt.show()
    return


if __name__ == "__main__":
    app.run()
