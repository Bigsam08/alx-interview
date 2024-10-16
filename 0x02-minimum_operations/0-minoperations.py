#!/usr/bin/python3
''' calculate the fewest no of operations needed to result in
exactly n H characters'''


def minOperations(n):
    ''' Returns fewest number of operations'''
    no_of_operations = 0
    mini = 2
    while n > 1:
        while n % mini == 0:
            no_of_operations += mini
            n /= mini
        mini += 1
    return no_of_operations
