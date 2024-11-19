#!/usr/bin/python3
''' A 2 x 2 2d matrix to rotate 90 degrees'''


def rotate_2d_matrix(matrix):
    ''' return none, asume matrix have 2 dimensions and is not empty'''
    matrix_len = len(matrix)
    for i in range(matrix_len):
        for v in range(i):
            initial_shape = matrix[i][v]
            matrix[i][v] = matrix[v][i]
            matrix[v][i] = initial_shape

    for i in range(matrix_len):
        for v in range(int(matrix_len/2)):
            temp = matrix[i][v]
            matrix[i][v] = matrix[i][matrix_len-1-v]
            matrix[i][matrix_len-1-v] = temp
