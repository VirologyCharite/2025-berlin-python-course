def evaluate(fields):
    value1, operator, value2 = fields

    # Convert to integers.
    value1 = int(value1)
    value2 = int(value2)

    if operator == "+":
        return value1 + value2
    elif operator == "-":
        return value1 - value2
    else:
        print("Sorry, I only know how to do addition or subtraction.")


def calculate():
    while True:
        line = input("Enter your command: ")

        if line == "q":
            print("Goodbye")
            break

        fields = line.split()

        if len(fields) == 3:
            print(evaluate(fields))
        else:
            print("Sorry, I am too dumb to deal with that. Please use 3 fields.")


calculate()
