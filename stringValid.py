# https://www.hackerrank.com/challenges/string-validators/problem
# Cheated a little and went to the discussion to find a way to not
# have to iterate over the entire string. I found any() and this
# is what I came up with from there.


def string_valid(string):
    print(any(char.isalnum() for char in string))
    print(any(char.isalpha() for char in string))
    print(any(char.isdigit() for char in string))
    print(any(char.islower() for char in string))
    print(any(char.isupper() for char in string))
