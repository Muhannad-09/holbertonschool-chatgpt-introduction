#!/usr/bin/python3
import sys

def factorial(n):
    """
    Recursively calculates the factorial of a non-negative integer.

    Parameters:
    n (int): A non-negative integer whose factorial is to be computed.

    Returns:
    int: The factorial of the input number.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Read input from the command line argument and compute factorial
f = factorial(int(sys.argv[1]))
print(f)
