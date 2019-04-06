# Classic Problems with Python (2019 Manning Press)
# Scratch Tests while skimming the book


def fib1(n: int) -> int:
    # Results in Max recursion error
    # todo: try except logic to avoid error?
    return fib1(n - 1) + fib1(n - 2)


if __name__ == "__main__":
    print(fib1(5))

