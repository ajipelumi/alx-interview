#!/usr/bin/python3
""" Lockboxes """


def canUnlockAll(boxes):
    """ Method that determines if all the boxes can be opened. """
    if len(boxes) == 0:
        return False

    # First key
    keys = [0]

    # Check if the key is in the box
    for key in keys:
        for newKey in boxes[key]:
            if newKey not in keys and newKey < len(boxes):
                keys.append(newKey)

    # Check if the number of keys is equal to the number of boxes
    if len(keys) == len(boxes):
        return True
    else:
        return False
