
# EAFP - Easier to ask for forgiveness than permission.

try:
    a = 3 + None
except TypeError:
    print("Sorry, can't do that.")
else:
    print(a)



# LBYL - Look before you leap.

b = None

if b is None:
    print("Sorry, can't do that.")
else:
    a = 3 + b

print(a)
