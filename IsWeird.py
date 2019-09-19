"""
Given an integer n, perform the following conditional actions:
If n is odd, print Weird
If n is even and in the inclusive range of 2 to 5, print Not Weird
If n is even and in the inclusive range of 6 to 20, print Weird
If n is even and greater than 20, print Not Weird
"""


def isWeird(n):
    weird = "Weird"
    not_weird = "Not Weird"

    if(n % 2):
        return weird
    if(20 < n):
        return not_weird
    if(6 <= n <= 20):
        return weird
    if(2 <= n <= 5):
        return not_weird
