#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """Compute the square value of all integers of a matrix."""
    new_matrix = []
    for col in matrix:
        result = list(map(lambda x: x**2, col))
        new_matrix.append(result)
    return ([list(map(lambda x: x * x, row)) for row in matrix])

    

