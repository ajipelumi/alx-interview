#!/usr/bin/python3
""" Minimum Operations Module. """


def minOperations(n):
    """ Minimum Operations Function. """
    if n <= 1:
        return 0

    # Declare minimum operation as 0
    min_operations = 0
    # Declare current length as 1 as we start with 1 character 'H'
    current_length = 1
    # Declare clipboard as 0 as we are not copying anything yet
    clipboard = 0

    # Loop until current length is equal to n
    while current_length < n:
        # If n is divisible by current length, we can copy all and paste
        if n % current_length == 0:
            # This is the only time we can copy
            clipboard = current_length
            # Minimum operation is incremented by 1 because we copied
            min_operations += 1

        # Paste the clipboard
        current_length += clipboard
        # Minimum operation is incremented by 1 because we pasted
        min_operations += 1

    # Return minimum operation
    return min_operations
