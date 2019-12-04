"""
The sum of the squares of the first ten natural numbers is,
12 + 22 + ... + 102 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

import math

n_1_to_10 = [n for n in range(1,11)]
n_1_to_100 = [n for n in range(1,101)]

def sum_of_squares(data):
    total = 0
    for elem in data:
        total += elem * elem
    return total

def squares_of_sum(data):
    total = 0
    for elem in data:
        total += elem
    return total * total

print("result:", squares_of_sum(n_1_to_10) - sum_of_squares(n_1_to_10))

print("result:", squares_of_sum(n_1_to_100) - sum_of_squares(n_1_to_100))