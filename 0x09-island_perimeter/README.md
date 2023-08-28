## Island Perimeter

### Description
This is a function that returns the perimeter of an island in a grid.

### Prototype
`def island_perimeter(grid)`
where `grid` is a list of lists of integers representing the island.

### Example:
```python
>>> grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
>>> island_perimeter(grid)
12
```

### Files:
[0-main.py](0-main.py)  
[0-island_perimeter.py](0-island_perimeter.py)

### Explanation
The function `island_perimeter` takes a grid as an argument and returns the perimeter of the island in the grid. The grid is a list of lists of integers. 
The perimeter is the sum of the number of edges of the island. The island is represented by 1s in the grid. The edges are the 0s surrounding the island.

We start by handling an empty grid. If the grid is empty, the perimeter is 0.
We then iterate through the grid, row by row. For each row, we iterate through the columns.

If the current cell is a 1, we check the cells above, below, to the left and to the right.
If the cell is a 0, we add 1 to the perimeter. 
If the cell is a 1, we do nothing. We do this for each cell in the grid.

After iterating through the grid, we return the perimeter.

### Big O Notation
`island_perimeter(grid)` has a time complexity of *O(n\*m)*, where *n* is the number of rows in the grid and *m* is the number of columns in the grid.
This is because there are two nested loops, one for the rows and one for the columns which means that the number of operations is proportional to the number of rows times the number of columns.

The space complexity is *O(1)* because we use a constant amount of space, regardless of the size of the input grid.
We only use the `perimeter` variable to store the perimeter of the island and this does not change with the size of the grid.