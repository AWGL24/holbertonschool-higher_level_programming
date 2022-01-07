#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newm = []
    for i in range(len(matrix)):
        newm.append(list(map(lambda x: x ** 2, matrix[i])))
    return(newm)
