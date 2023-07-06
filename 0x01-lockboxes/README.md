## Lockboxes

### Description
This is a function that determines if all the boxes in a list of lists can be opened.

### Prototype
`def canUnlockAll(boxes)`
where `boxes` is a list of lists.

### Example:
```python
>>> canUnlockAll([[1], [2], [3], [4], []])
True

>>> canUnlockAll([[1, 2], [3, 4], [1, 2], [3, 4]])
False

>>> canUnlockAll([[4], [3], [2], [1], [0]])
True

>>> canUnlockAll([[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]])
True

>>> canUnlockAll([[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]])
False
```

### Files:
[0-main.py](0-main.py)
[0-lockboxes.py](0-lockboxes.py)

### Explanation:
The function `canUnlockAll` returns `True` if all the boxes can be opened or `False` if not.

The function takes a list of lists called `boxes` as input.
Each list in `boxes` represents a box, and the indices of the lists represent the keys that can open the box.

The first box in `boxes` is always unlocked.
The function checks if all the boxes can be opened by starting from the first box and checking if the keys in that box can open any other boxes.

If a key can open a box, the function adds the keys in that box to a list called `keys`.

The function then checks if the keys in `keys` can open any other boxes.
If a key can open a box, the function adds the keys in that box to `keys`.

The function continues to check if the keys in `keys` can open any other boxes until there are no more keys that can open any other boxes.

If all the boxes can be opened, the function returns `True`.
If not, the function returns `False`.