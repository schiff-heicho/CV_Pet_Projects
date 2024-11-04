import keyboard
import time
import graph

def Game(array, size, size_cell, window):
    x = 0 #координаты стрелочки в лабиринте по x
    y = 0 #координаты стрелочки в лабиринте по y   
    graph.CreatePointer(x, y, size_cell, window, "red")
    while True:
        key = keyboard.read_key()
        if key == "esc":
            window.close()
            return
        if key == "d" and array[y][x][1] == 0:
            graph.CreatePointer(x, y, size_cell, window, "grey")
            x += 1
        if key == "w" and array[y][x][2] == 0:
            graph.CreatePointer(x, y, size_cell, window, "grey")
            y -= 1
        if key  == "s" and array[y][x][3] == 0:
            graph.CreatePointer(x, y, size_cell, window, "grey")
            y += 1
        if key == "a" and array[y][x][0] == 0:
            graph.CreatePointer(x, y, size_cell, window, "grey")
            x -= 1
        if x == size - 1 and y == size - 1:
            window.close()
            return            
        graph.CreatePointer(x, y, size_cell, window, "red")
        time.sleep(0.17)