
# Define a function is_palindrome() that recognizes palindromes (i.e. words that look the same written backwards).
# For example, is_palindrome("radar") should return True.


def is_palindrome(string):

    if string == string[::-1]:
        return True
    else:
        return False


print(is_palindrome("racecar"))
print(is_palindrome("hello"))