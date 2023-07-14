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

The function starts with a string called `s` that contains one `H` character.

The function checks if `n` is equal to `0` or `1`.
If `n` is equal to `0` or `1`, the function returns `0`.

If `n` is greater than `1`, the function checks if `n` is divisible by `2`.
If `n` is divisible by `2`, the function divides `n` by `2` and adds `2` to the number of operations.

If `n` is not divisible by `2`, the function checks if `n` is divisible by `3`.
If `n` is divisible by `3`, the function divides `n` by `3` and adds `3` to the number of operations.

If `n` is not divisible by `2` or `3`, the function adds `1` to the number of operations and adds `1` `H` character to `s`.

The function continues to check if `n` is divisible by `2` or `3` until `n` is equal to `1`.

The function returns the number of operations.