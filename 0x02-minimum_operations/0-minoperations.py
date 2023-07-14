#!/usr/bin/python3
""" Minimum Operations Module. """


def minOperations(n):
    """ Minimum Operations Function. """
    if n <= 1:
        return 0

    # Set min_op to 0
    min_op = 0
    # Iterate from 2 to n
    i = 2
    # While n is less than or equal to n
    while i <= n:
        # If n is divisible by i
        if n % i == 0:
            # Add i to min_op
            min_op += i
            # Divide n by i
            n = n / i
        else:
            # Increment i
            i += 1
    # Return min_op
    return min_op
