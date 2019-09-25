# https://www.hackerrank.com/challenges/find-a-string/problem
# Count the substring occurances in larger string
# While list comprehension is a more efficient method, I find it
# harder to read so I've used a less efficient solution that's
# easier for me to read.


def count_substring(string, sub_string):
    count = 0

    for i in range(len(string)):
        if sub_string == string[i:i+len(sub_string)]:
            count += 1

    return count
