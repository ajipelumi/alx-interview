#!/usr/bin/python3
""" Prime Game. """


def isPrime(num):
    """ Checks if num is a prime number. """
    # 0 and 1 are not prime numbers
    if num < 2:
        return False
    # 2 is the only even prime number
    if num == 2:
        return True
    # All other even numbers are not prime
    if num % 2 == 0:
        return False
    # Check odd numbers from 3 to sqrt(num)
    # (num + 1 because range is exclusive)
    for i in range(3, int(num**0.5) + 1, 2):
        # If num is divisible by i, it's not prime
        if num % i == 0:
            return False
    # If we get here, num is prime
    return True


def isWinner(x, nums):
    """ Determine who the winner of each game is. """
    # Initialize scores
    maria = 0
    ben = 0
    # Iterate through rounds
    for _ in range(x):
        # Get the first number in nums
        n = nums.pop(0)
        # If n is less than or equal to 1, ben wins the round by default
        if n <= 1:
            # Add 1 to ben's score
            ben += 1
        else:
            # Initialize prime count
            prime_count = 0
            # Iterate through numbers from 2 to n + 1
            # (n + 1 because range is exclusive)
            for i in range(2, (n + 1)):
                # We only care about prime numbers within n
                # If i is prime, add 1 to prime count
                if isPrime(i):
                    prime_count += 1
            # Here we have the total number of prime numbers within n
            # If prime count is even, it means that ben wins the round
            if prime_count % 2 == 0:
                # Add 1 to ben's score
                ben += 1
            else:
                # Here, maria wins the round so add 1 to her score
                maria += 1

    # After all rounds, if maria's score is greater than ben's, she wins
    if maria > ben:
        return "Maria"
    # If ben's score is greater than maria's, he wins
    elif ben > maria:
        return "Ben"
    # If both scores are equal, it's a tie so return None
    else:
        return None
