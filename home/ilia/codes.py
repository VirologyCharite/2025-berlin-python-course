import marimo

__generated_with = "0.14.16"
app = marimo.App(width="medium")


@app.cell
def _():
    def __init__(self, id, sequence):
        self.id = id
        self.sequence = sequence



    def __len__(self):
        return len(self.sequence)


    def reverse_complement (self):
        pass


    def find(self, pattern):
        pass
    return


if __name__ == "__main__":
    app.run()
