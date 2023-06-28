## Pascal's Triangle

### Description
This is a function that returns a list of lists of integers representing the Pascal’s triangle of n.

### Prototype
`def pascal_triangle(n)`
where `n` is the number of rows of Pascal's triangle to return.

### Example:
```python
>>> pascal_triangle(0)
[]
>>> pascal_triangle(1)
[1]
>>> pascal_triangle(2)
[1]
[1, 1]
>>> pascal_triangle(3)
[1]
[1, 1]
[1, 2, 1]
>>> pascal_triangle(4)
[1]
[1, 1]
[1, 2, 1]
[1, 3, 3, 1]
>>> pascal_triangle(5)
[1]
[1, 1]
[1, 2, 1]
[1, 3, 3, 1]
[1, 4, 6, 4, 1]
```

### Files:
[0-main.py](0-main.py)
[0-pascal_triangle.py](0-pascal_triangle.py)

### Explanation:
This [code](0-pascal_triangle.py) defines a function called `pascal_triangle` that creates Pascal's triangle.
Pascal's triangle is a triangular arrangement of numbers, where each number is the sum of the two numbers directly above it.
The function takes a number `n` as input and returns the corresponding Pascal's triangle as a list of lists.

To create the triangle, the code uses a concept called a matrix, which is like a table with rows and columns.
The matrix is initially empty.

The code then starts a loop that will run `n` times. Each iteration of the loop represents a row in the triangle.

Inside the loop, the code defines an empty list called `row`, which represents the current row of numbers.

Another loop is started that runs `i + 1` times.
The `i` here represents the current row number, and since counting starts from 0, we add 1 to include the appropriate number of columns for the current row.

Within this inner loop, the code checks if the current column is the first column or the last column of the row.
If it is, then the value 1 is appended to the `row` list.
These 1's represent the edges of Pascal's triangle, where the numbers are always 1.

If the current column is not an edge column, then the code calculates the value for that position by adding the corresponding numbers from the previous row.
The calculated value is then appended to the `row` list.

After the inner loop completes for a `row`, the row list is added to the `matrix` list, which represents the entire Pascal's triangle.

Once the outer loop finishes iterating through all the rows, the `matrix` list containing all the rows of Pascal's triangle is returned as the final result.