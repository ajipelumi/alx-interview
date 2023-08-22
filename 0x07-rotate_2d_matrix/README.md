## Rotate 2D Matrix

### Description
This is a function that rotates a 2D matrix 90 degrees clockwise.

### Prototype
`def rotate_2d_matrix(matrix)`
where `matrix` is a 2D matrix.

### Example:
```python
>>> matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
>>> rotate_2d_matrix(matrix)
>>> print(matrix)
[[7, 4, 1],
 [8, 5, 2],
 [9, 6, 3]]
```

### Files:
[0-main.py](0-main.py)  
[0-rotate_2d_matrix.py](0-rotate_2d_matrix.py)

### Explanation:
The function `rotate_2d_matrix` rotates a 2D matrix 90 degrees clockwise.

Firstly, we get the length of the matrix, which is the number of rows in the matrix. We will use this length to iterate through the matrix.

Then, we iterate through the matrix, and for each row, we iterate through the elements in the row. We transpose and reverse the matrix in place.

For example, if we have the matrix:
```python
[[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]]
```
We transpose it to get:
```python
[[1, 4, 7],
 [2, 5, 8],
 [3, 6, 9]]
```
Then, we reverse each row to get:
```python
[[7, 4, 1],
 [8, 5, 2],
 [9, 6, 3]]
```
`n - 1 - row` ensures that we reverse the rows as we transpose the matrix.

After transposing and reversing the matrix, we update the original matrix with the new matrix. The function does not return anything because we are updating the original matrix.