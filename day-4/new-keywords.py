def divide(a, b):
    assert b != 0, "Cannot divide by zero"
    return a / b


print(divide(3, 7))
# print(divide(3, 0))


def add_x_but_only_once(numbers, x):
    numbers_already_processed = set()

    # Skip the number using continue.
    for number in numbers:
        if number in numbers_already_processed:
            continue
        print(number + x)
        numbers_already_processed.add(number)

    # Skip the number using not.
    for number in numbers:
        if number not in numbers_already_processed:
            print(number + x)
        numbers_already_processed.add(number)

    # Skip the number using pass.
    for number in numbers:
        if number in numbers_already_processed:
            pass
        else:
            print(number + x)
            numbers_already_processed.add(number)


add_x_but_only_once((4, 7, 4, 99), 100)


def print_numbers(numbers):
    print(f"Prining the numbers in {numbers}")
    for i in numbers:
        if type(i) is int:
            print(i)
        else:
            # print(f"Hey, {i} is not an integer!")
            raise ValueError(f"{i} is not an integer!")


try:
    print_numbers((3, 77, "Thursday", 1000))
except ValueError as error:
    print("Oops, looks like something went wrong...", error)


def numbers_between_dumb(a, b):
    "Return the numbers from a to b-1"
    result = []
    current_number = a
    while current_number < b:
        result.append(current_number)
        current_number += 1

    return result


# This is a "generator" !
def numbers_between_one_at_a_time(a, b):
    print(f"Generating numbers from {a} to {b-1}.")
    "Return the numbers from a to b-1"
    current_number = a
    while current_number < b:
        yield current_number
        current_number += 1

# This is a "generator" !
def numbers_greater_than(a):
    print(f"Generating numbers greater than {a}.")
    while True:
        a += 1
        yield a


limit = 20
count = 0

print("---------------------------------")
print("HERE 1")
# numbers = numbers_between_one_at_a_time(45, 5700000000)
numbers = numbers_greater_than(450)
print(numbers)
print("HERE 2")

for number in numbers:
    print("HERE 3")
    count += 1
    if count == limit:
        break

    print(number)
