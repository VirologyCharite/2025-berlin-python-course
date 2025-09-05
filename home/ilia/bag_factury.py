import marimo

__generated_with = "0.14.16"
app = marimo.App(width="medium")


@app.cell
def _(color, length):
    class bag:
   
        def __init__(self, color, lenghth=10, width=10, hight=10):
            print(f"Making a bag.")
       
            self.color = color
            self.lenghth = length
            self.width = width
            self.hight = hight
            self.volume = width*lenghth*hight

        def volume(self):
            return self.lenghth * self.width * self.hight

        my_purple_bag = color("purple")
    
        print(my_purple_bag.color)
        print(my_purple_bag.volume())
    

    return


if __name__ == "__main__":
    app.run()
