
# Define a function that computes the length of a given list or string. (It is true that Python has the
#  len() function built in, but writing it yourself is nevertheless a good exercise.)


def find_length(string):

    length = 0
    for i in string:
        length += 1
    return length


print(find_length("Happy Birthday"))

print(len("Happy Birthday"))
