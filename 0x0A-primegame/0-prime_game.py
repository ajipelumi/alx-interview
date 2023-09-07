#!/usr/bin/python3
""" Prime Game. """


def isPrime(num):
    """ Checks if num is a prime number. """
    # 0 and 1 are not prime numbers
    if num < 2:
        return False
    # 2 is a prime number
    if num == 2:
        return True
    # Check if num is divisible by any number from 2 to num - 1
    for i in range(2, num):
        # If divisible, num is not prime
        if num % i == 0:
            return False
    # If not divisible, num is prime
    return True


def isWinner(x, nums):
    """ Determine who the winner of each game is. """
    # Initialize scores
    maria = 0
    ben = 0
    # Iterate through each game
    for i in range(len(nums)):
        # Initialize prime count
        prime_count = 0
        # Iterate through each number in the game
        for j in range(1, nums[i] + 1):
            # If prime, increment prime count
            if isPrime(j):
                prime_count += 1
        # If prime count is even, increment Ben's score
        if prime_count % 2 == 0:
            ben += 1
        # If prime count is odd, increment Maria's score
        else:
            maria += 1
    # If Maria's score is greater, return Maria
    if maria > ben:
        return "Maria"
    # If Ben's score is greater, return Ben
    elif ben > maria:
        return "Ben"
    # If scores are equal, return None
    else:
        return None
    