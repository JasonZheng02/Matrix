from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 255, 255, 0 ]
matrixY = new_matrix(0,0)
matrixR = new_matrix(0,0)
matrixB = new_matrix(0,0)
matrixO = new_matrix(0,0)

#Yellow
x = 200
while x < 250:
    add_edge(matrixY, x,300,0, x,350,0)
    x = x + 1

x = 150
while x < 300:
    add_edge(matrixY, x,100,0, x,300,0)
    x = x + 1

draw_lines( matrixY, screen, color )

#Red
color = [ 255, 0, 0 ]
x = 210
while x < 220:
    add_edge(matrixR, x,330,0, x,340,0)
    x = x + 1

draw_lines( matrixR, screen, color )

#Blue
color = [ 51, 171, 249]
x = 230
while x < 245:
    add_edge(matrixB, x,325,0, x,340,0)
    x = x + 1

draw_lines( matrixB, screen, color )

#Orange
color = [ 255, 102, 0]
x = 180
y = 0
z = 2.25
while x < 270:
    add_edge(matrixO, x,200 - int(y),0, x,200 + int(y),0)
    x = x + 1
    y = y + z
    z = z - 0.05

draw_lines( matrixO, screen, color )
display(screen)
