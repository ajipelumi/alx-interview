#!/usr/bin/python3
""" Making Change. """


def makeChange(coins, total):
    """ Making Change. """
    # Check if total is 0 or negative
    if total <= 0:
        return 0

    # Check if coins is empty
    if len(coins) == 0:
        return -1

    # Initialize change counter
    change = 0
    # Get the max coin
    max_coin = max(coins)
    # Loop until total is 0
    while total > 0:
        print(f"This is the total: {total}")
        print(f"This is the max coin: {max_coin}")
        # Check if total is greater than max coin
        if total >= max_coin:
            # Subtract max coin from total
            total -= max_coin
            # Add 1 to change counter
            change += 1
        else:
            # Check if coins is more than 1
            if len(coins) > 1:
                # Remove max coin from coins
                coins.remove(max_coin)
                # Get the new max coin
                max_coin = max(coins)
            else:
                # When length of coins is less than or equal to 1
                # It means that the total cannot be made from the coins
                return -1

    # Check if total is 0
    if total == 0:
        # Return change counter
        return change
    else:
        return -1
