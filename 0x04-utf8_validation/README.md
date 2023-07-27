## UTF8 Validation

### Description
This is a function that determines if a given data set represents a valid UTF-8 encoding.

### Prototype
`def validUTF8(data)`
where `data` is a list of integers.

### Example:
```python
>>> data = [65]
>>> validUTF8(data)
True

>>> data = [65, 256]
>>> validUTF8(data)
False

>>> data = [65, 256, 0]
>>> validUTF8(data)
True

>>> data = [65, 256, 0, 0, 0]
>>> validUTF8(data)
True
```

### Files:
[0-main.py](0-main.py)
[0-validate_utf8.py](0-validate_utf8.py)

### Explanation:
The function `validUTF8` returns `True` if the data set represents a valid UTF-8 encoding, otherwise returns `False`.

The function checks if the data is None or empty, if it is, it returns `False`.

The function iterates through the data set, and for each integer converts it to binary and stores it in a binary list.

We then iterate through the binary list, and for each binary number we check what it starts with.

If it starts with `0`, we pop it from the binary list and continue to the next binary number.

If it starts with `110`, we check the length that the length of the binary list is greater than 1, and that the next binary number starts with `10`, if it does, we pop both numbers from the binary list and continue to the next binary number, otherwise we return `False`.

If it starts with `1110`, we check the length that the length of the binary list is greater than 2, and that the next two binary numbers start with `10`, if they do, we pop the three numbers from the binary list and continue to the next binary number, otherwise we return `False`.

If it starts with `11110`, we check the length that the length of the binary list is greater than 3, and that the next three binary numbers start with `10`, if they do, we pop the four numbers from the binary list and continue to the next binary number, otherwise we return `False`.

If the binary number starts with anything else, we return `False`.

If we reach the end of the binary list, we return `True`.