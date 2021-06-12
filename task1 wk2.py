class PrimeIterator:
    """Class to generate prime numbers from 1 to a number n"""

    def __init__(self, n):
        self.start = 1
        self.n = n

    def is_prime(self, num):
        if num <= 1:
            return
        for i in range(2, num):
            if num % i == 0:
                return
        return True

    def __iter__(self):
        self.current_value = self.start
        return self

    def __next__(self):
        for number in range(self.current_value, self.n):
            if self.is_prime(number):
                self.current_value = number + 1
                return number
        raise StopIteration


prime = PrimeIterator(10)

j = iter(prime)

print(next(j))
print(next(j))
print(next(j))
print(next(j))
print(next(j))


