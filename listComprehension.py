# Problem called for list comprehension that was longer than Pep8 standart
# This throws a warning in linted IDEs


def non_sum_coordinates(x, y, z, non_sum):
    return [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if((i+j+k) != non_sum)]
