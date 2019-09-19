"""
You are given the year:
You have to write a function to check if the year is a leap year or not.
"""


def is_leap(year):
    leap = False

    if not(year % 4):
        leap = True
    if not(year % 100) and (year % 400):
        leap = False

    return leap
