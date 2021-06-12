class PrimeIterator:
    """Class to generate prime numbers from 1 to a number n"""

    def __init__(self, n):
        self.lower = 1
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        for num in range(self.lower, self.n+1):
            if num > 1:
                for i in range(2, num):
                    if num % i == 0:
                        break
                else:
                    return num
        else:
            raise StopIteration


prime = PrimeIterator(5)

j = iter(prime)

print(next(j))
print(next(j))
print(next(j))




































# class PrimeIter:
#     def __init__(self):
#         self.current = 1
#
#     def next(self):
#         self.current = self.current + 1
#         while 1:
#             for i in range(2, self.current/2 + 1):
#                 if self.current % i == 0:
#                     self.current = self.current + 1
#                     break # Break current for loop
#             else:
#                 break # Break the while loop and return
#         return self.current
#
#     def __iter__(self):
#         return self
#
# if __name__ == '__main__':
#     p = PrimeIter()
#     for p in range (5):
#         print(p)