from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 0, 0 ]
matrix = new_matrix(0,0)
add_edge(matrix, 10,495,0, 55,455,0 )
add_edge(matrix, 85,455,0, 55,495,0 )

draw_lines( matrix, screen, color )
display(screen)
