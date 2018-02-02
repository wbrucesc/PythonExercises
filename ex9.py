

# Write a function is_member() that takes a value (i.e. a number, string, etc) x and a list of values a, and returns
# True if x is a member of a, False otherwise. (Note that this is exactly what the in operator does, but for the sake
# of the exercise you should pretend Python did not have this operator.)


def is_member(x, a):

    for i in a:
        if x == i:
            return True

    return False


print(is_member(2, [1, 2, 3]))
print(is_member("Will", ["Costa", "Myers", "Will", "Mike", "Debbie"]))

