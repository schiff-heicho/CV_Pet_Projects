import tkinter as tk
import graphics as gr

def PrintLabirint(array, size, size_cell, window):
    for i in range(size):
        for j in range(size):
            if array[i][j][2]:
                my_line = gr.Line(gr.Point(10 + size_cell * j, 10 + size_cell * i), gr.Point( 10 + size_cell * (j + 1), 10 + size_cell * i))
                my_line.draw(window)
            if array[i][j][1] and (i != size - 1 or j != size - 1):
                my_line = gr.Line(gr.Point(10 + size_cell * (j + 1), 10 + size_cell * i), gr.Point(10 + size_cell * (j + 1), 10 + size_cell * (i+ 1)))
                my_line.draw(window)                
            if array[i][j][3]:
                my_line = gr.Line(gr.Point(10 + size_cell * j, 10 + size_cell * (i + 1)), gr.Point(10 + size_cell * (j + 1), 10 + size_cell * (i + 1)))
                my_line.draw(window)                
            if array[i][j][0]:
                my_line = gr.Line(gr.Point(10 + size_cell * j, 10 + size_cell * i), gr.Point(10 + size_cell * (j), 10 + size_cell * (i + 1)))
                my_line.draw(window)                

def CreatePointer(x, y, size_cell, window, color):
    pointer = gr.Line(gr.Point(10 + size_cell * x , 10 + size_cell * y), gr.Point(10 + size_cell * (x + 1), 10 + size_cell * (y + 1)))
    pointer.setFill(color)
    pointer.draw(window)
    pointer = gr.Line(gr.Point(10 + size_cell * x , 10 + size_cell * (y + 1)), gr.Point(10 + size_cell * (x + 1), 10 + size_cell * y))
    pointer.setFill(color)
    pointer.draw(window)