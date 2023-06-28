#!/usr/bin/python3
"""
Pascal's Triangle
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal’s triangle of n
    """
    # Define matrix
    matrix = []

    # Iterate n times (rows)
    for i in range(n):

        # Define row list
        row = []

        # Iterate i + 1 times (columns) because i starts at 0
        for j in range(i + 1):

            # If first or last column, append 1 to row
            if j == 0 or j == i:
                row.append(1)
            else:  # else, append sum of previous row's columns
                sum = matrix[i - 1][j - 1] + matrix[i - 1][j]
                row.append(sum)

        # Append row to matrix
        matrix.append(row)

    return matrix  # Return matrix
