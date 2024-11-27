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
    if coins == [] or coins is None:
        return -1
    try:
        coinIdx = coins.index(total)
        return 1
    except ValueError:
        pass

    coins.sort(reverse=True)
    count = 0
    for i in coins:
        if total % 1 == 0:
            count += int(total / i)
            return count
        if total - i >= 0:
            if int(total / i) > 1:
                count += int(total / i)
                total = total % i
            else:
                count = count + 1
                total = total - 1
                if total == 0:
                    break
    if total > 0:
        return -1
    return count
