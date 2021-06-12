import argparse
import functools


def get_month_decorator(func):
    @functools.wraps(func)
    def inner(n):
        if n > 12 or n < 1:
            raise argparse.ArgumentTypeError("Enter a number between 1 and 12")
        result = func(n)
        return result

    return inner


@get_month_decorator
def new_month(n):
    a = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August",
         9: "September", 10: "October", 11: "November", 12: "December"}

    for month in a:
        if month == n:
            break
    return a[n]


b = new_month(13)
print(b)
