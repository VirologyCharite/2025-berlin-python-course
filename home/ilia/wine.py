import marimo

__generated_with = "0.14.16"
app = marimo.App(width="medium")


@app.cell
def _():
    import pandas as pd
    wine = pd.read_csv("/data/wine.csv")


    import matplotlib.pyplot as plt
    x = wine["alcohol"]
    y = wine["residual sugar"]

    plt.scatter(x, y)
    plt.xlabel('percent')
    plt.ylabel('Y Values')

    plt.title ('Wine Scatter Plot')
    plt.show()
    return (wine,)


@app.cell
def _(wine):
    wine

    return


@app.cell
def _(alt, wine):
    # replace _df with your data source
    _chart = (
        alt.Chart(wine)
        .mark_point()
        .encode(
            x=alt.X(field='residual sugar', type='quantitative'),
            y=alt.Y(field='free sulfur dioxide', type='quantitative', aggregate='mean'),
            color=alt.Color(field='citric acid', type='quantitative'),
            tooltip=[
                alt.Tooltip(field='residual sugar', format=',.2f'),
                alt.Tooltip(field='free sulfur dioxide', aggregate='mean', format=',.2f'),
                alt.Tooltip(field='citric acid', format=',.2f')
            ]
        )
        .properties(
            height=290,
            width='container',
            config={
                'axis': {
                    'grid': True
                }
            }
        )
    )
    _chart
    return


@app.cell
def _():
    import altair as alt
    return (alt,)


if __name__ == "__main__":
    app.run()
