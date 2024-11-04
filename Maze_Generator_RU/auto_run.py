import graph
import time
def GoLabirint2(array, size, line, column, size_cell, window):
    direction = 1
    while column != size - 1 or line != size -1:
        time.sleep(0.01)
        graph.CreatePointer(column, line, size_cell, window, "grey")
        if  direction == 1: 
            if array[line][column][1] == 0 and array[line][column][3] == 1: #идём вправо
                column += 1
                graph.CreatePointer(column, line, size_cell, window, "red")
            elif array[line][column][1] == 1 and array[line][column][3] == 1:
                direction = 2
            else:
                line += 1
                direction = 3
                graph.CreatePointer(column, line, size_cell, window, "red")
            continue
        if  direction == 0: 
            if array[line][column][0] == 0 and array[line][column][2] == 1: #идём вправо
                column -= 1
                graph.CreatePointer(column, line, size_cell, window, "red")
            elif array[line][column][0] == 1 and array[line][column][2] == 1:
                direction = 3
            else:
                line -= 1
                direction = 2
                graph.CreatePointer(column, line, size_cell, window, "red")
            continue
        if  direction == 2: 
            if array[line][column][2] == 0 and array[line][column][1] == 1: #идём вправо
                line -= 1
                graph.CreatePointer(column, line, size_cell, window, "red")
            elif array[line][column][2] == 1 and array[line][column][1] == 1:
                direction = 0
            else:
                column += 1
                direction = 1
                graph.CreatePointer(column, line, size_cell, window, "red")
            continue
        if  direction == 3: 
            if array[line][column][3] == 0 and array[line][column][0] == 1: #идём вправо
                line += 1
                graph.CreatePointer(column, line, size_cell, window, "red")
            elif array[line][column][3] == 1 and array[line][column][0] == 1:
                direction = 1
            else:
                column -= 1
                direction = 0
                graph.CreatePointer(column, line, size_cell, window, "red")
            continue