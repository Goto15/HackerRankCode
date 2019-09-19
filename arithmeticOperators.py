"""
Read two integers from STDIN and print three lines where:

The first line contains the sum of the two numbers.
The second line contains the difference of the two numbers (first - second).
The third line contains the product of the two numbers.
"""


def sum(n, m):
    return n+m


def difference(n, m):
    return n-m


def product(n, m):
    return n*m


def arithmetic_operators(n, m):
    print(sum(n, m))
    print(difference(n, m))
    print(product(n, m))
