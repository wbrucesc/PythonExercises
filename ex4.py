
# Write a function that takes a character (i.e. a string of length 1) and returns True if it is a vowel,
#  False otherwise.


def is_vowel(letter):

    vowels = ["a", "e", "i", "o", "u"]
    if letter in vowels:
        return True
    else:
        return False


# print(is_vowel("o"))
# print(is_vowel("z"))
