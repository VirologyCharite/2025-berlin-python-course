import marimo

__generated_with = "0.14.16"
app = marimo.App(width="medium")


@app.cell
def _():
    import pandas as pd
    tips = pd.read_excel("/data/tips.xlsx")
    tips_csv = pd.read_csv("/data/tips.csv")

    import matplotlib.pyplot as plt
    x = tips["total_bill"]
    y = tips["tip"]
    sex = tips["sex"]

    #colors = ['blue if s = 'Male' else 'red' for s in sex]

    colors = []
    for s, bill, tip in zip(sex, x, y):
        if tip / bill >= 0.1:
            color = "green"
        elif s == "Male":
            color = "blue"
        else:
            color ="red"
        colors.append(color)
    
    plt.scatter(x, y)
    plt.xlabel('X Values')
    plt.ylabel('Y Values')

    plt.title ('Basic Scatter Plot')

    plt.scatter([], [], c='blue', label='Male')
    plt.scatter([], [], c='red', label='Female')

    plt.show
    return


if __name__ == "__main__":
    app.run()
