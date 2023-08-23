#!/usr/bin/python3
""" Log parsing. """
import sys


# Initialize file size, line count and status codes
file_size = 0
line_count = 0
status_codes = {"200": 0, "301": 0, "400": 0, "401": 0,
                "403": 0, "404": 0, "405": 0, "500": 0}


def print_stats():
    """ Print stats. """
    # Print file size
    print("File size: {}".format(file_size))
    # Sort status codes and print them if they are greater than 0
    for key in sorted(status_codes.keys()):
        if status_codes[key] > 0:
            print("{}: {}".format(key, status_codes[key]))


# Try to read stdin line by line
try:
    for line in sys.stdin:
        # Split line by spaces
        split = line.split()
        # Check if split has at least 2 elements
        if len(split) > 2:
            # Get file size
            file_size += int(split[-1])
            # Get status code
            status_code = split[-2]
            # Check if status code is in status_codes
            if status_code in status_codes:
                # Increment status code
                status_codes[status_code] += 1
        # Increment line count
        line_count += 1
        # Check if line count is multiple of 10
        if line_count % 10 == 0:
            # Print stats
            print_stats()
except KeyboardInterrupt:
    # Print stats
    print_stats()
    raise
