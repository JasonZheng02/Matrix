from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 0, 0 ]
matrix = new_matrix(0,0)
#stick figure
add_edge(matrix, 10,5,0, 55,45,0 )
add_edge(matrix, 85,5,0, 55,45,0 )
add_edge(matrix, 55,45,0, 55,150,0 )
add_edge(matrix, 25,150,0, 85,150,0 )
add_edge(matrix, 25,150,0, 25,210,0 )
add_edge(matrix, 85,150,0, 85,210,0 )
add_edge(matrix, 25,210,0, 85,210,0 )
add_edge(matrix, 55,90,0, 20,120,0 )
add_edge(matrix, 55,90,0, 90,120,0 )

#sword
add_edge(matrix, 70,125,0, 93,105,0 )
add_edge(matrix, 70,125,0, 115,165,0 )
add_edge(matrix, 93,105,0, 138,145,0 )

draw_lines( matrix, screen, color )
display(screen)
