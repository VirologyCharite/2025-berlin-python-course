import marimo

__generated_with = "0.14.16"
app = marimo.App(width="medium")


@app.cell
def _():
    import matplotlib.pyplot as plt
    import pandas as pd
    import plotly.express as px
    return plt, px


@app.cell
def _(px):
    # tips = pd.read_excel("/data/tips.xlsx")
    tips = px.data.tips()
    return (tips,)


@app.cell
def _(tips):
    x = tips["total_bill"]
    y = tips["tip"]
    sex = tips["sex"]

    colors = []
    tip_fraction = []

    for s, bill, tip in zip(sex, x, y):
        fraction = tip / bill
        tip_fraction.append(fraction)
        if fraction >= 0.2:
            color = "green"
        elif s == "Male":
            color = "blue"
        else:
            color = "red"

        colors.append(color)
    return colors, tip_fraction, x


@app.cell
def _(colors, plt, tip_fraction, x):
    plt.scatter(x, tip_fraction, c=colors)

    plt.xlabel('Total bill (dollars)')
    plt.ylabel('Tip (dollars)')
    plt.title('Basic Scatter Plot')

    # Crappy way to make a legend...
    plt.scatter([], [], c='blue', label='Male')
    plt.scatter([], [], c='red', label='Female')
    plt.legend()

    plt.show()
    return


if __name__ == "__main__":
    app.run()
