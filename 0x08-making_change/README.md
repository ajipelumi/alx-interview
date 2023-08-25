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

A while loop is used to iterate through the list `coins` and check if the total is greater than or equal to the value of the maximum coin.
If so, the total is decremented by the value of the maximum coin and the variable `change` is incremented by 1.

After incrementing `change`, the new total is checked to see if it is less than `max_coin` as that would mean that the new total is less than the value of the largest coin.
If so, the `max_coin` is removed from the list `coins` and the variable `max_coin` is updated to the new largest coin in the list and the while loop is repeated.

Once the while loop is finished, the function returns the value of `change`.
If the total is not 0, it means that the total could not be made with the coins in the list `coins` and the function returns -1.

### Big O Notation
**makeChange** has a worst-case time complexity of *O(n)*, where `n` is the number of coins in the list `coins`.
The function's primary operations, such as finding the largest coin, decrementing the total, and incrementing the change variable, are all executed in constant time.
The loop's number of iterations is determined by the relationship between `total` and the maximum coin value `max_coin`.
In cases where `total` is much larger than `max_coin`, the loop may run for a relatively small number of iterations.
This leads to a practical time complexity of *O(n)* for most scenarios involving manageable values of total and max_coin.