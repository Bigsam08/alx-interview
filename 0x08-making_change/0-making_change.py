#!/usr/bin/python3
""" coin of different values, determine fewest
numer of coins needed to meet the given total
"""


def makeChange(coins, total):
    ''' Function to set the project going
    coins is a list of values
    return: fewest number of coins to meet total
    '''
    if total <= 0:
        return 0
    if not coins:
        return -1
    try:
        if total in coins:
            return 1
    except ValueError:
        pass

    coins.sort(reverse=True)
    count = 0
    for coin in coins:
        while total >= coin:
            total -= coin
            count += 1
        if total == 0:
            return count
    return -1 if total > 0 else count
