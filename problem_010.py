"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
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


data = sieve(2_000_000)
print("data length:", len(data) )
total = 0
for elem in data:
    total += elem
print(total)

