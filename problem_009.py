"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

import math

def find_triplet(limit, added):
    for a in range(1,limit):
        if a % 10 == 0:
            print(a)
        for b in range(1,limit):
            for c in range(1,limit):
                if a + b + c == added:
#                    print("a:", a, "b:", b, "c:", c, "a2:" , a * a, "b2:", b * b, "c2:", c * c, "a2 + b2:", a*a + b*b)
                    if (a * a + b * b) == c * c:
                        print("result:", a, b, c)
                        return [a, b, c]

result = find_triplet(500, 1000) #500 is an educated guess

print(result)
print(result[0] * result[1] * result[2])