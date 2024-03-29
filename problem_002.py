"""
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""
import math

limit = 4_000_000

Phi    = 1.618033988749894848204586834365638117720309179805762
phi    = 1 - Phi
root_5 = 2.236067977499789696409173668731276235440618359611525

def euler(n):
    result = math.pow(Phi, n) - math.pow(phi, n)
    result = result / root_5
    return int(round(result))

data = []

for index in range(1,1000):
    number = euler(index)
    if number < limit and number % 2 == 0:
        data.append(number)

print(sum(data))
#answer: 4613732