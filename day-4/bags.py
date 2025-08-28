from random import choice


class Bag:

    COLORS = ("lilac", "pink", "dark blue", "light blue", "black", "white")

    def __init__(self, color=None, length=30, width=30, height=30, waterproof=False):
        if color is None:
            self.color = choice(self.COLORS)
            # print("No color was requested, so I randomly chose", self.color)
        else:
            self.color = color
            # print(f"Making a {color} bag!")
        self.length = length
        self.width = width
        self.height = height
        self.waterproof = waterproof

    def __str__(self):
        return f"A {self.color} bag with length {self.length} and volume {self.volume()}."

    def __gt__(self, other_bag):
        return self.volume() > other_bag.volume()

    def volume(self):
        return self.width * self.length * self.height

    def is_waterproof(self):
        return self.waterproof


my_purple_bag = Bag(color="purple")
print(my_purple_bag.color, my_purple_bag.length, my_purple_bag.volume())


my_wide_bag = Bag(width=100)
print(f"My wide bag has a volume of", my_wide_bag.volume())

my_green_bag = Bag("green")
print(my_green_bag)

if my_wide_bag > my_purple_bag:
    print("Wide bag is bigger")
else:
    print("Purple is bigger")
