#!/usr/bin/python3
''' A Prime number game using python
a game between two players
n: is a random range number provided for each round
x: is the number of times bothe players plays'''


def isWinner(x, nums):
    ''' A game between Maria and Ben
    x: number of rounds
    nums: an array of n
    n: is the range of provided number'''

    if x < 1 or not nums:
        return None
    ben = 0
    maria = 0
    n = max(nums)
    prime_number = [True] * (n + 1)
    prime_number[0], prime_number[1] = False, False
    for i in range(2, n + 1):
        if prime_number[i]:
            for j in range(i * 2, n + 1, i):
                prime_number[j] = False
    for round_count in nums:
        prime_count = sum(prime_number[:round_count])
        if prime_count % 2 == 0:
            ben += 1
        else:
            maria += 1
        if maria == ben:
            return None
    return 'Maria' if maria > ben else 'Ben'
