## Prime Game

### Description
This is a function that determines the winner of a prime game.

### Prototype
`def isWinner(x, nums)`
where `x` is the number of rounds and `nums` is a list of `n` non-negative integers.

### Example:
```python
>>> x = 5
>>> nums = [0, 1, 2, 3, 4, 5]
>>> isWinner(x, nums)
Ben
```

### Files:
[0-main.py](0-main.py)  
[0-prime_game.py](0-prime_game.py)

### Explanation
The function `isWinner` takes two arguments, `x` and `nums`. `x` is the number of rounds and `nums` is a list of `n` non-negative integers.

The function returns the name of the player that won the most rounds. If the winner cannot be determined, `None` is returned.

We start by initializing `maria` and `ben` to `0`. We then iterate `x` times, each time we initialize `n` to the first element of `nums` and remove it from the list.

We then check if `n` is less than or equal to 1, if it is, we increment `ben` as this means that `maria` cannot make a move.

Otherwise, we check if `n` is prime and initialize a counter to track the number of prime numbers less than or equal to `n`.

We then iterate from `2` to `n + 1` and check if the current number is prime, if it is, we increment the counter.

If the counter is even, we increment `ben` as this means that Ben will win the round, otherwise, we increment `maria`.

After the loop, we check if `maria` is greater than `ben`, if it is, we return `Maria`, if `ben` is greater than `maria`, we return `Ben`, otherwise, we return `None`.

### Big O Notation
We run `x`` rounds, and in each round, we check numbers up to `n + 1`.
For each number, we determine if it's prime, which takes `O(sqrt(n))` time.
Overall, this gives us a time complexity of `O(x * n * sqrt(n))`.
In terms of space, we use `O(1)` space since we don't create large data structures that grow with input size.