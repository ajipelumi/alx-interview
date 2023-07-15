## Minimum Operations

### Description
This is a function that determines the fewest number of operations needed to result in exactly `n` `H` characters in a file.

### Prototype
`def minOperations(n)`
where `n` is an integer.

### Example:
```python
>>> minOperations(4)
4

>>> minOperations(12)
7

>>> minOperations(9)
6

>>> minOperations(0)
0

>>> minOperations(1)
0
```

### Files:
[0-main.py](0-main.py)
[0-minoperations.py](0-minoperations.py)

### Explanation:
The function `minOperations` returns the fewest number of operations needed to result in exactly `n` `H` characters in a file.

The function takes an integer called `n` as input.

The function returns `0` if `n` is less than or equal to `1`.

The function declares a variable called `min_operations` and sets it to `0`.

The function declares a variable called `current_length` and sets it to `1` (the length of the string `H`).

The function declares a variable called `clipboard` and sets it to `0` as the clipboard is initially empty.

While `current_length` is less than the input `n`, the function checks if `n` is divisible by `current_length`.
If `n` is divisible by `current_length`, the function sets `clipboard` to `current_length` and increments `min_operations` by `1` as this is a copy operation.

The function then sets `current_length` to `current_length` plus `clipboard` as this is a paste operation and increments `min_operations` by `1` as this is a paste operation.

If `n` is not divisible by `current_length`, the function increments `current_length` by `clipboard` as this is a paste operation and increments `min_operations` by `1` as a result.

The function returns `min_operations` as the fewest number of operations needed to result in exactly `n` `H` characters in a file.