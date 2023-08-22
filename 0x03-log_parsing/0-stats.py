#!/usr/bin/python3
""" Log parsing. """
import sys


def print_stats(file_size, status_codes):
    """ Print stats. """
    # Print file size
    print("File size: {}".format(file_size))
    # Sort status codes and print them if they are greater than 0
    for key in sorted(status_codes.keys()):
        if status_codes[key] > 0:
            print("{}: {}".format(key, status_codes[key]))


if __name__ == "__main__":
    # Initialize file size and status codes
    file_size = 0
    status_codes = {"200": 0, "301": 0, "400": 0, "401": 0,
                    "403": 0, "404": 0, "405": 0, "500": 0}
    # Try to read stdin line by line
    try:
        for i, line in enumerate(sys.stdin, 1):
            # Split line into words
            data = line.split()
            # Get file size which is the last word of the line
            file_size += int(data[-1])
            # Get status code which is the second to last word of the line
            if data[-2] in status_codes:
                status_codes[data[-2]] += 1
            # Print stats every 10 lines
            if i % 10 == 0:
                print_stats(file_size, status_codes)
    except KeyboardInterrupt:
        # Print stats when Ctrl+C is pressed
        print_stats(file_size, status_codes)
        # Raise the exception again to exit
        raise
