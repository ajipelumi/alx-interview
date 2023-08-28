## Making Change

### Description
This is a function that determines the fewest number of coins needed to meet a given amount total.

### Prototype
`def makeChange(coins, total)`
where `coins` is a list of the values of the coins in your possession and `total` is the amount of money to be made.

### Example:
```python
>>> coins = [1, 2, 25]
>>> total = 37
>>> makeChange(coins, total)
7
```

### Files:
[0-main.py](0-main.py)  
[0-making_change.py](0-making_change.py)

### Explanation
The function `makeChange` determines the fewest number of coins needed to meet a given amount total.

**makeChange** checks if the total is less than or equal to 0. If so, it returns 0.

The function then initializes a variable `change` to the value of 0.
A variable `max_coin` is initialized to the value of the largest coin in the list `coins`.

A while loop is used to iterate until the total is less than or equal to 0.
Within the loop, we check if the total is greater than or equal to the value of `max_coin`.
If so, we decrement the total by the value of `max_coin` and increment the value of `change` by 1.

If not, we check if the coins list is greater than 1. This is to avoid an infinite loop in cases where the total is less than the value of `max_coin`.
If the coins list is greater than 1, we remove the largest coin from the list and reassign `max_coin` to the new largest coin.

If the coins list is not greater than 1, it means that the total is less than the value of `max_coin` and that the total cannot be made with the coins in the list as we have reached the smallest coin in the list so we return -1.

After the loop, we check if the total is equal to 0. If so, we return the value of `change`.
If not, it means that the total cannot be made with the coins in the list so we return -1.
The if statement is an extra check to ensure that the function returns -1 in cases where the total is less than the value of `max_coin` and the coins list is not greater than 1.

### Big O Notation
**makeChange** has a worst-case time complexity of *O(n)*, where `n` is the number of coins in the list `coins`.
The function's primary operations, such as finding the largest coin, decrementing the total, and incrementing the change variable, are all executed in constant time.
The loop's number of iterations is determined by the relationship between `total` and the maximum coin value `max_coin`.
In cases where `total` is much larger than `max_coin`, the loop may run for a relatively small number of iterations.
This leads to a practical time complexity of *O(n)* for most scenarios involving manageable values of total and max_coin.