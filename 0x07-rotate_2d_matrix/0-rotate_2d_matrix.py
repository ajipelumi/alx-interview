#!/usr/bin/python3
""" Rotate 2D Matrix. """


def rotate_2d_matrix(matrix):
    """ Rotate 2D Matrix. """
    # Get the length of the matrix.
    n = len(matrix)
    # Create a new matrix with the same dimensions as the original.
    result = [[0] * n for _ in range(n)]
    # Iterate through the matrix rows.
    for row in range(n):
        # Iterate through the matrix columns.
        for col in range(n):
            # We first transpose the matrix, then we reverse each row.
            # n - 1 - row ensures that we reverse the rows as we transpose.
            result[col][n - 1 - row] = matrix[row][col]
    # Iterate through the matrix rows.
    for row in range(n):
        # Iterate through the matrix columns.
        for col in range(n):
            # We assign the result to the original matrix.
            matrix[row][col] = result[row][col]
