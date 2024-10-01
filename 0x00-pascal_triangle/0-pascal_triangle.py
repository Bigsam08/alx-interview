#!/usr/bin/python3
"""
building a pascal_triangle function.

"""


def pascal_triangle(n):
    """
    returns empty list if n <= 0
    returns list of integers forming a pascal_triangle

    """

    empty_list = []
    if n <= 0:
        return empty_list

    empty_list = [[1]]
    for a in range(1, n):
        first = [1]
        for b in range(len(empty_list[a - 1]) - 1):
            second = empty_list[a - 1]
            first.append(empty_list[a - 1][b] + empty_list[a - 1][b + 1])
        first.append(1)
        empty_list.append(first)

    return empty_list
