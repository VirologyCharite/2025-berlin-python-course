import marimo

__generated_with = "0.14.16"
app = marimo.App(width="medium")


@app.cell
def _():
    import pandas as pd
    tips = pd.read_csv("/data/tpis.csv")

    return


if __name__ == "__main__":
    app.run()
