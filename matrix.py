"""
A matrix will be an N sized list of 4 element lists.
Each individual list will represent an [x, y, z, 1] point.
For multiplication purposes, consider the lists like so:
x0  x1      xn
y0  y1      yn
z0  z1  ... zn
1  1        1
"""
import math

#print the matrix such that it looks like
#the template in the top comment
def print_matrix( matrix ):
    bucket = []
    for r in matrix[0]:
        bucket.append("")
    for c in matrix:
        for r in range(len(c)):
            #print(str(c[r]))
            bucket[r] += str(c[r])
    for i in range(len(bucket)):
        print(bucket[i])

#turn the paramter matrix into an identity matrix
#you may assume matrix is square
def ident( matrix ):
    n = len(matrix)
    x = len(matrix[0])
    if n != x:
        print("not square matrix")
        return
    for c in range(n):
        for r in range(n):
            if  c == r:
                matrix[c][r] = 1
            else:
                matrix[c][r] = 0

#multiply m1 by m2, modifying m2 to be the product
#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    cols = len(m2)
    rows = len(m1)
    for r in range(cols):
        for c in range(rows):

    pass


def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
