from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix()
matrix2 = new_matrix()

matrix2[0][0] = 2

ident(matrix)
matrix_mult(matrix, matrix2)
print_matrix(matrix)

draw_lines( matrix, screen, color )
display(screen)
