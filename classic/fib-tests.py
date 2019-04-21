# Classic Problems with Python (2019 Manning Press)
# Scratch Tests while skimming the book

import sys
from typing import Dict
from typing import Generator
from functools import lru_cache

memo: Dict[int, int] = {0: 0, 1: 1}  # our base cases for fib3


def fib1(n: int) -> int:
    # Results in Max recursion error
    # todo: try except logic to avoid error?
    return fib1(n - 1) + fib1(n - 2)


def fib2(n: int) -> int:
    #todo: add counter to track # of function calls

    if n < 2:  # base case to avoid excessive recursion error
        return n
    return fib2(n - 2) + fib2(n - 1)  # recursive case


def fib3(n: int) -> int:
    if n not in memo:
        memo[n] = fib3(n - 1) + fib3(n - 2)  # memoization
    return memo[n]


@lru_cache(maxsize=None)
def fib4(n: int) -> int:  # same definition as fib2()  Decorator caches each return value
    if n < 2:  # base case
        return n
    return fib4(n - 2) + fib4(n - 1)  # recursive case


def fib5(n: int) -> int:
    if n == 0: return n  # special case
    last: int = 0  # initially set to fib(0)
    next: int = 1  # initially set to fib(1)
    for _ in range(1, n):
        last, next = next, last + next
    size = sys.getsizeof(n)   #test to see size of the variable
    print('size of n ',size)

    return next


def fib6(n: int) -> Generator[int, None, None]:
    yield 0  # special case
    if n > 0: yield 1  # special case
    last: int = 0  # initially set to fib(0)
    next: int = 1  # initially set to fib(1)
    for _ in range(1, n):
        last, next = next, last + next
        yield next  # main generation step


if __name__ == "__main__":
    print('\nfib2 approach')
    print(fib2(5))
    print(fib2(30))  # takes a few seconds to run these 50000+ calls
#    timeit.timeit(fib2(30))  #measure time for function that just printed

    print('\nfib3 approach')
    print(fib3(5))
    print(fib3(50))

    print('\nfib4 approach')
    print(fib4(5))
    print(fib4(50))

    print('\nfib5 approach')
    print(fib5(5))
    print(fib5(50))

    print('\nfib6 approach\n')
    for i in fib6(50):
        print(i)


# -30-