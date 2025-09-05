import marimo

__generated_with = "0.14.16"
app = marimo.App(width="medium")


app._unparsable_cell(
    r"""
    class Bag:
        def _init_(self,color, length=10, width=10,height=10):
            print (f\"Making a {color}colored bag\")
            self.color = color
            self.length = length
            self.width = width
            self.height = height

        def volume(self)
    """,
    name="_"
)


if __name__ == "__main__":
    app.run()
