"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
import math


def check_palindrome(number):
    is_palindrome = True
    str_num = str(number)
    size = len(str_num)
    half_size = math.floor(size/2)
    for index in range(0, half_size + 1):
        char_1 = str_num[index]
        char_2 = str_num[size - index-1]
        if char_1 != char_2:
            is_palindrome = False
    return is_palindrome

print(check_palindrome(21923))

all = []
for xx in range(999, 1, -1):
    for yy in range(999, 1, -1):
        val = xx * yy
        if check_palindrome(val):
            print("first:", xx, "second:", yy, "=", val)
            all.append(val)

print(max(all))
#answer: 906609