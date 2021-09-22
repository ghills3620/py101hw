# - Write a function that takes a single argument, prints the value of
# the argument, and returns the argument as a string.

val = input("enter value here ")
print(val)


# - Write a function that takes a variable number of arguments and
# prints them all.

def multi_input(*argv):
    for arg in argv:
        print(arg)


multi_input('Multiple', 'inputs', 'can', 'be', 'placed', 'here')


# - Write a function that prints the names and values of keyword
# arguments passed to it.

def key_value_pairs(**kwargs):
    for key, value in kwargs.items():
        print("%s : %s" % (key, value))


key_value_pairs(first='Geeks', mid='for', last='Geeks')

# - Write a python script (file) that prints your name as all lower case, upper case and proper capitalization.
# (Bonus) if you can pass in your name: input()? argparse? etc

name = input('Type name')


def name_changeer(name):
    print(name.capitalize())
    print(name.upper())
    print(name.lower())
    print(name.title())


name_changeer(name)
