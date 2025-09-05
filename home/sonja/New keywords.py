import marimo

__generated_with = "0.14.16"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    def divide(a,b):
        assert b!= 0   b can not be 0! asserting a statement. 
    error gives you back info on which assertion was violated.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""raise ValueError("Oops, something is wrong")  raising an error and showing it - creating an exception""")
    return


app._unparsable_cell(
    r"""

    from random import choice  #randomizing

    COLORS = ( \"lilac\", \"pink\", dark blue\")

    #class is a factory, creating objects that can have attributes and functions

    class Bag:     #class is a factory that can make bags,
          def __init__(self,color = None, length, width, heighth, waterproof = False):    #init is a function we define, self is an object, __init__ has to be with double unerscored, self is the way to call it
          if color is None:
             self.color = choice(COLORS)
              print(\"No color was requested, so I used\")
          self.color = color  #atribute has to be defined here!!!
          self.length = 30
          self.waterproof = waterproof

          def volume(self):
              return self.width * self.length * self.heigth

        def __str__(self):   #used on objects to print them
        

        def __gt__(self, other bag):  #function to evaluate greater than
        



    mybag = Bag(\"purple\")

    print(mybag.color)   #color is an atribute
    print(my_purple_bag.volume())   #() because volume is a function we need to call
    \"\"\"
    )
    """,
    name="_"
)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r""" """)
    return


if __name__ == "__main__":
    app.run()
