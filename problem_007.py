"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

def sieve(n: int) -> list:
    """
    Sieve away and only primes are left.
    """
    primes = 2*[False] + (n-1)*[True]
    for i in range(2, int(n**0.5+1.5)):
        for j in range(i*i, n+1, i):
            primes[j] = False
    return [prime for prime, checked in enumerate(primes) if checked]


data = sieve(1000000)
print("data length:", len(data) )

print(data[6 - 1]) #there is an obiwan problem here
print(data[10001 -1])