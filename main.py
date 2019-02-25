from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix()

print("\nnew matrix:")
print_matrix(matrix)

print("\nidentity matrix:")
ident(matrix)

print_matrix(matrix)


m0 = [ [1,4,7],[2,5,8],[3,6,9]]
m1 = [ [4,10,3],[12,5,6],[7,8,1]]
print("\nmatrix A")
print_matrix(m0)
print("\nmatrix B")
print_matrix(m1)
print("\nmultiplying A * B puts the result in B and gives:")
matrix_mult(m0,m1)
print_matrix(m1)
#print("\n")
#print_matrix(m0)

# expect
#  33  40  26
#  84 109  74
# 135 178 122



for i in range(250):
    for j in range(500):
        if ( (125-i)*(125-i)/16 == (500-j) ):
            add_edge(matrix, i,j,1,i,j+20,1)
            add_edge(matrix, i+250,j,1,i+250,j+20,1)
            add_edge(matrix, i,500-j,1,i,480-j,1)
            add_edge(matrix, i+250,500-j,1,i+250,480-j,1)
        if ( (125-j)*(125-j)/16 == (500-i) ):
            add_edge(matrix, i,j,1,i+20,j,1)
            add_edge(matrix, i,j+250,1,i+20,j+250,1)
            add_edge(matrix, 500-i,j,1,480-i,j,1)
            add_edge(matrix, 500-i,j+250,1,480-i,j+250,1)
            
draw_lines( matrix, screen, color )

save_extension(screen,"art.png")
print("\nimage file created")
print("art.png")
