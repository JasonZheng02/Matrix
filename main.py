from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix(4,4)
matrix2 = new_matrix(4,4)

matrix[0][0] = 6
matrix[0][1] = 6
matrix[2][1] = 6
matrix[2][3] = 6
matrix[3][2] = 6
matrix[1][2] = 10
matrix[3][0] = 10
matrix2[0][2] = 8
matrix2[1][0] = 8
matrix2[2][1] = 8
matrix2[3][3] = 8
matrix2[0][1] = 28
matrix2[3][2] = 28

# ident(matrix)
matrix2 = matrix_mult(matrix, matrix2)
print_matrix(matrix2)
# resulting matrix
# 48	168	 48	 0
#  0	 80	  0	 0
# 48	  0	168	48
#  0	328	 80	 0
draw_lines( matrix2, screen, color )
display(screen)
