#!/usr/bin/python3
""" UTF-8 Validation Module. """


def validUTF8(data):
    """ Determines if a given data set represents a valid UTF-8 encoding. """
    if not data or len(data) == 0:
        return False

    bin_list = []
    # Iterate over data and convert to binary
    for character in data:
        bin_list.append(format(character, '#010b')[-8:])

    # Check if binary is valid
    for binary in bin_list:
        # Check if binary is 1 byte
        if binary[0] == '0':
            # If it is, binary is valid and we can continue
            # to the next element in the list so we pop it
            bin_list.pop(0)
            continue

        # Check if binary is 2 bytes
        elif binary[:3] == '110':
            # If it is, check that binary list has at least 2 elements
            if len(bin_list) < 2:
                return False
            # Check that the next element in the list starts with 10
            if bin_list[1][:2] != '10':
                return False
            # We pop the first 2 bytes of the binary
            bin_list.pop(0)
            bin_list.pop(0)

        # Check if binary is 3 bytes
        elif binary[:4] == '1110':
            # If it is, check that binary list has at least 3 elements
            if len(bin_list) < 3:
                return False
            # Check that the next 2 elements in the list start with 10
            if bin_list[1][:2] != '10' or bin_list[2][:2] != '10':
                return False
            # We pop the first 3 bytes of the binary
            bin_list.pop(0)
            bin_list.pop(0)
            bin_list.pop(0)

        # Check if binary is 4 bytes
        elif binary[:5] == '11110':
            # If it is, check that binary list has at least 4 elements
            if len(bin_list) < 4:
                return False
            # Check that the next 3 elements in the list start with 10
            if bin_list[1][:2] != '10' or bin_list[2][:2] != '10' \
                    or bin_list[3][:2] != '10':
                return False
            # We pop the first 4 bytes of the binary
            bin_list.pop(0)
            bin_list.pop(0)
            bin_list.pop(0)
            bin_list.pop(0)

        # If binary is not 1, 2, 3, or 4 bytes, it is invalid
        else:
            return False

    return True
