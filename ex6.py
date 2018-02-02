
# Define a function sum() and a function multiply() that sums and multiplies (respectively) all the numbers in a list of
# numbers. For example, sum([1, 2, 3, 4]) should return 10, and multiply([1, 2, 3, 4]) should return 24.


def add(args):

    result = 0
    for i in args:
        result += i

    return result


# print(add([1, 2, 3, 5]))

def multiply(args):

    result = 1
    for i in args:
        result *= i

    return result


# print(multiply([2, 5]))
