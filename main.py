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
x = 0
while x < 3:
    add_edge(matrix, 70 + x,125,0, 93 + x,105,0 )
    add_edge(matrix, 70 + x,125,0, 115 + x,165,0 )
    add_edge(matrix, 93 + x,105,0, 138 + x,145,0 )
    add_edge(matrix, 80 + x,200,0, 115 + x,165,0 )
    add_edge(matrix, 173 + x,110,0, 138 + x,145,0 )
    add_edge(matrix, 80 + x,200,0, 430 + x,490,0 )
    add_edge(matrix, 173 + x,110,0, 420 + x,297,0 )
    add_edge(matrix, 430 + x,490,0, 420 + x,297,0 )
    x = x + 1

draw_lines( matrix, screen, color )
display(screen)
