from math import sqrt
from itertools import takewhile, count


class Main:

    @staticmethod
    def is_prime(n):
        for i in range(2, round(sqrt(n))+1):
            if n % i == 0:
                return False
        return True

    def prime_gen(self):
        for i in count():
            if self.is_prime(i):
                yield i

    def __init__(self, n):
        primes = takewhile(lambda x: x**2 < n, self.prime_gen())
        print(', '.join(str(i) for i in primes))
