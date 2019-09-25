# https://www.hackerrank.com/challenges/python-mutations/problem
# replace a character at a specific, given index
# I used slicing since I love it


def replace_char(string, position, character):
    return string[:position] + character + string[position+1:]
