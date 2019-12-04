"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""


primes_of_1_to_10 = [2, 3, 5, 7]
primes_of_1_to_10_to_produce_all = [2, 2, 2, 3, 3, 5, 7]

def mult_all(data):
    total = 1
    for index in data:
        total *= index
    return total

print(2 * 3 * 5 * 7)

def check_divisibility(number):
    for divisor in range(2, 11):
        if number % divisor != 0:
            print(divisor)

print(mult_all(primes_of_1_to_10_to_produce_all))
print(check_divisibility(mult_all(primes_of_1_to_10)))
print(check_divisibility(mult_all(primes_of_1_to_10_to_produce_all)))

primes_of_1_to_20 = [2, 3, 5, 7, 11, 13, 17, 19]
primes_of_1_to_20_to_produce_all = [2, 2, 2, 2, 3, 3, 5, 7, 11, 13, 17, 19]

print("just all primes in 1 to 20 multiplied:", mult_all(primes_of_1_to_20))
print(check_divisibility(mult_all(primes_of_1_to_20)))

print("just all primes in 1 to 20 multiplied to produce:", mult_all(primes_of_1_to_20_to_produce_all))
print(check_divisibility(mult_all(primes_of_1_to_20_to_produce_all)))

