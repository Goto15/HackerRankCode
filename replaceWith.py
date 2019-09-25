# https://www.hackerrank.com/challenges/python-string-split-and-join/problem
# The answer wants a split and then join with characters, but replace() is much
# easier to read answer.


def spaces_to_dashes(string):
    return string.replace(" ", "-")
