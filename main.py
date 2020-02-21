from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 255, 255, 0 ]
matrixY = new_matrix(0,0)
matrixR = new_matrix(0,0)

x = 200
while x < 250:
    add_edge(matrixY, x,300,0, x,350,0)
    x = x + 1

x = 150
while x < 300:
    add_edge(matrixY, x,100,0, x,300,0)
    x = x + 1

color = [ 255, 0, 0 ]
x = 210
while x < 220:
    add_edge(matrixR, x,340,0, x,350,0)
    x = x + 1

draw_lines( matrixY, screen, color )
draw_lines( matrixR, screen, color )
display(screen)
