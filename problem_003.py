"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

import math

def primeFactors(n):
    result = []
    # Print the number of two's that divide n
    no_two_yet = True
    while n % 2 == 0:
        if no_two_yet:
            result.append(2)
            no_two_yet = False
        n = n / 2


    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
    for i in range(3, int(math.sqrt(n)) + 1, 2):

        # while i divides n , print i ad divide n
        while n % i == 0:
            if not n in result:
                result.append(i)
            n = n / i

            # Condition if n is a prime
    return result

list = primeFactors(600851475143)

print(list)
#answer: 6857