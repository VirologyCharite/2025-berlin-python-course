import marimo

__generated_with = "0.14.16"
app = marimo.App(width="medium")


@app.cell
def _():
    import pandas as pd
    import matplotlib.pyplot as plt

    tips = pd.read_excel("/data/tips.xlsx")  # load excel file
    # tips = pd.read_csv("/data/tips.csv")  

    # pull two columns as x and y values
    x = tips["total_bill"]
    y = tips["tip"]
    sex = tips["sex"]

    colors = ['blue' if s == "Male" else 'red' for s in sex] 
    # colors = []
    # tip_fraction = []
    #for s, bill, tip in zip(sex, x, y)
        # fraction = tip/bill
        # tip_fraction = append.(fraction)
        #if tip / bill >= 0.2:
            #color = "green"
        #if s == "Male"'":
            #colors.append("blue")
        #else:
            #colors.append("red")

    plt.scatter(x, y, c=colors)
    plt.scatter([], [], c='blue', label='Male')
    plt.scatter([], [], c='red', label='Female')
    plt.xlabel("Total bill ($)")
    plt.ylabel("Tip ($)")
    plt.title("Title of scatter plot")
    plt.legend()
    plt.show()
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
