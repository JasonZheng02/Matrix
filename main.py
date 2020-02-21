from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 255, 255, 0 ]
matrix = new_matrix(0,0)

x = 200
while x < 300:
    add_edge(matrix, x,300,0, x,400,0)
    x = x + 1

draw_lines( matrix, screen, color )
display(screen)
