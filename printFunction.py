"""
Read an integer n.

Without using any string methods, try to print the following:
123 ... n
Note that "..." represents the values in between. 
"""


def count_to_n(n):
    for i in range(0, n):
        print(i, end='')
