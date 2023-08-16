#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = matrix.copy()
    n = len(new) 
    for i in range(n): 
            new[i] = list(map(lambda x: x**2,new[i])) 
    return new 
