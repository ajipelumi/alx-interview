#!/usr/bin/python3
""" Making Change. """


def makeChange(coins, total):
    """ Making Change. """
    # Check if total is 0 or negative
    if total <= 0:
        return 0

    # Initialize change counter
    change = 0
    # Get the max coin
    max_coin = max(coins)
    # Loop until total is 0
    while total >= max_coin:
        # Subtract max coin from total
        total -= max_coin
        # Increment change counter by 1
        change += 1
        # Check if total is now less than max coin
        if total < max_coin:
            # Remove max coin from coins list
            coins.remove(max_coin)
            # Get new max coin
            max_coin = max(coins)

    # Check if total is 0
    if total == 0:
        # Return change counter
        return change
    else:
        # Return -1 if total cannot be made with coins
        return -1
