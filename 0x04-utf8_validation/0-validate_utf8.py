#!/usr/bin/python3
""" UTF-8 Validation Module. """


def validUTF8(data):
    """ Determines if a given data set represents a valid UTF-8 encoding. """
    # Check if data exists or is not empty
    if not data or len(data) == 0:
        return False

    # Define an index to iterate through the data
    index = 0
    # While the index is less than the length of the data
    while index < len(data):
        # Convert the current data element to binary
        binary = format(data[index], '#010b')[-8:]

        # If the first bit is 0, move to the next element
        if binary[0] == '0':
            index += 1
        # If the first bit is 1, check the number of 1s
        elif binary[:3] == '110':
            # If the next element does not start with 10, return False
            if index + 1 >= len(data) or format(data[index + 1],
                                                '#010b')[0:2] != '10':
                return False
            # Move to the next 2 elements
            index += 2
        # If the first 3 bits are 1, check the number of 1s
        elif binary[:4] == '1110':
            # If the next 2 elements do not start with 10, return False
            if index + 2 >= len(data) or format(data[index + 1],
                                                '#010b')[0:2] != '10' \
                    or format(data[index + 2], '#010b')[0:2] != '10':
                return False
            # Move to the next 3 elements
            index += 3
        # If the first 4 bits are 1, check the number of 1s
        elif binary[:5] == '11110':
            # If the next 3 elements do not start with 10, return False
            if index + 3 >= len(data) or format(data[index + 1],
                                                '#010b')[0:2] != '10' \
                    or format(data[index + 2], '#010b')[0:2] != '10' \
                    or format(data[index + 3], '#010b')[0:2] != '10':
                return False
            # Move to the next 4 elements
            index += 4
        else:
            # If the first 5 bits are 1, return False
            return False

    # If all checks pass, return True
    return True
