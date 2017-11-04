
# Write a function translate() that will translate a text into "rövarspråket" (Swedish for "robber's language").
#  That is, double every consonant and place an occurrence of "o" in between. For example, translate("this is fun")
#  should return the string "tothohisos isos fofunon".

from ex4 import is_vowel


def translate(string):

    results = []
    for word in string.split():
        result = ""
        for letter in word:
            if is_vowel(letter):
                result += letter
            else:
                result += letter + "o" + letter
        results.append(result)

    return ' '.join(results)


print(translate("Happy Birthday"))


