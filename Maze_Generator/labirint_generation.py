import random
def CreateArray(array, size):
    for i in range(size):
        array.append([])  #строка лабиринта
        for j in range(size):
            array[i].append([1, 1, 1, 1]) # j клетка в строке i, хранит наличие у неё всех стенок 0 лево/1 право/2 верх/3 низ
            
def CreateArrayUse(size, array): #массив хранящий заходили мы в клетку или нет
    for i in range(size):
        array.append([])
        for j in range(size):
            array[i].append(0)

def DFS(array, size, line, column, array_color):
    array_color[line][column] = 1
    array_random = [0, 1, 2, 3]
    for i in range(4):
        order = array_random[random.randint(0, 3 - i)]
        array_random.remove(order)
        if  order == 0 and line != size - 1 and array_color[line + 1][column] == 0: #идём вниз
            array[line][column][3] = 0
            array[line + 1][column][2] = 0
            DFS(array, size, line + 1, column, array_color)
        if  order == 1 and column != size - 1 and array_color[line][column + 1] == 0: #идём вправо
            array[line][column][1] = 0
            array[line][column + 1][0] = 0
            DFS(array, size, line, column + 1, array_color)
        if  order == 2 and line != 0 and array_color[line - 1][column] == 0: #идём вверх
            array[line][column][2] = 0
            array[line - 1][column][3] = 0
            DFS(array, size, line - 1, column, array_color)
        if  order == 3 and column != 0 and array_color[line][column - 1] == 0: #идём влево
            array[line][column][0] = 0
            array[line][column - 1][1] = 0
            DFS(array, size, line, column - 1, array_color)
                
def OldasAlgoritm(array, size, line, column, array_color, count):
    while count < size ** 2 - 1:
        array_color[line][column] = 1
        order = random.randint(0, 3)
        if  order == 0 and line != size - 1: #идём вниз
            if array_color[line + 1][column] == 0:
                array[line][column][3] = 0
                array[line + 1][column][2] = 0
                count += 1
            line += 1
        if  order == 1 and column != size - 1: #идём вправо
            if array_color[line][column + 1] == 0:
                array[line][column][1] = 0
                array[line][column + 1][0] = 0
                count += 1
            column += 1
        if  order == 2 and line != 0: #идём вверх
            if array_color[line - 1][column] == 0:
                array[line][column][2] = 0
                array[line - 1][column][3] = 0
                count += 1
            line -= 1
        if  order == 3 and column != 0: #идём влево
            if array_color[line][column - 1] == 0:
                array[line][column][0] = 0
                array[line][column - 1][1] = 0
                count += 1
            column -= 1


def OstovTree(array, size):
    for i in range(size - 1, -1, -1):
        for j in range(size - 1, -1, -1):
            order = random.randint(0, 1)
            if i == size - 1 and j != size - 1:
                array[i][j][1] = 0
                array[i][j + 1][0] = 0
            if j == size - 1 and i != size - 1:
                array[i][j][3] = 0
                array[i + 1][j][2] = 0
            if i != size - 1 and order == 0:
                array[i][j][3] = 0
                array[i + 1][j][2] = 0
            if j != size - 1 and order == 1:
                array[i][j][1] = 0
                array[i][j + 1][0] = 0
                
def Change_index(value):
    if value == 0:
        return 1
    if value == 1:
        return 0
    if value == 2:
        return 3
    if value == 3:
        return 2
    
def DeleteCicle(connected, connected_transition, array, line, column):
    index = connected.index([line, column]) + 1
    for i in range(index - 1, len(connected_transition)):
        array[connected[i][0]][connected[i][1]][connected_transition[i]] = 1
        array[connected[i + 1][0]][connected[i + 1][1]][Change_index(connected_transition[i])] = 1 #функция перевода индеска стенки в обратн
    connected = connected[:index]
    connected_transition = connected_transition[:index - 1]
    return index

def Portition(array_not_use):
    pivot = random.randint(0, len(array_not_use) - 1)
    pivot_value = array_not_use[pivot]
    return pivot_value

def CreateArrayNotUse(size, array_not_use):
    for i in range(size):
        for j in range(size):
            array_not_use.append([i, j])
    
def Uinston(array, size, array_not_use, array_color):
    count = 1
    pivot = Portition(array_not_use)
    array_color[pivot[0]][pivot[1]] = 1
    array_not_use.remove([pivot[0], pivot[1]])
    while count < size ** 2:
        pivot = Portition(array_not_use)
        connected = [pivot]
        line = pivot[0]
        column = pivot[1]
        connected_transition = []
        while count < size ** 2:
            order = random.randint(0, 3)
            if  order == 0 and line != size - 1: #идём вниз
                if array_color[line + 1][column] == 1:
                    array[line][column][3] = 0
                    array[line + 1][column][2] = 0
                    for i in range(len(connected)):
                        array_color[connected[i][0]][connected[i][1]] = 1
                        array_not_use.remove([connected[i][0], connected[i][1]])                  
                    count += len(connected)
                    break
                if [line + 1, column] in connected: 
                    line += 1                    
                    index = DeleteCicle(connected, connected_transition, array, line, column)
                    connected = connected[:index]
                    connected_transition = connected_transition[:index - 1]                    
                else:
                    array[line][column][3] = 0
                    array[line + 1][column][2] = 0
                    connected_transition.append(3)
                    connected.append([line + 1, column])
                    line += 1
                        
            if  order == 1 and column != size - 1: #идём вправо
                if array_color[line][column + 1] == 1:
                    array[line][column][1] = 0
                    array[line][column + 1][0] = 0
                    for i in range(len(connected)):
                        array_color[connected[i][0]][connected[i][1]] = 1
                        array_not_use.remove([connected[i][0], connected[i][1]])
                    count += len(connected)
                    break
                if [line, column + 1] in connected:
                    column += 1                  
                    index = DeleteCicle(connected, connected_transition, array, line, column)
                    connected = connected[:index]
                    connected_transition = connected_transition[:index - 1]                    
                else:
                    array[line][column][1] = 0
                    array[line][column + 1][0] = 0
                    connected_transition.append(1)
                    connected.append([line, column + 1])
                    column += 1      
            if  order == 2 and line != 0: #идём вверх
                if array_color[line - 1][column] == 1:
                    array[line][column][2] = 0
                    array[line - 1][column][3] = 0
                    for i in range(len(connected)):
                        array_color[connected[i][0]][connected[i][1]] = 1
                        array_not_use.remove([connected[i][0], connected[i][1]])
                    count += len(connected)
                    break
                if [line - 1, column] in connected:
                    line -= 1                    
                    index = DeleteCicle(connected, connected_transition, array, line, column)
                    connected = connected[:index]
                    connected_transition = connected_transition[:index - 1]                   
                else:
                    array[line][column][2] = 0
                    array[line - 1][column][3] = 0
                    connected_transition.append(2)
                    connected.append([line - 1, column])
                    line -= 1
            
            if  order == 3 and column != 0: #идём влево
                if array_color[line][column - 1] == 1:
                    array[line][column][0] = 0
                    array[line][column - 1][1] = 0
                    for i in range(len(connected)):
                        array_color[connected[i][0]][connected[i][1]] = 1
                        array_not_use.remove([connected[i][0], connected[i][1]])
                    count += len(connected)
                    break
                if [line, column - 1] in connected:
                    column -= 1                   
                    index = DeleteCicle(connected, connected_transition, array, line, column)
                    connected = connected[:index]
                    connected_transition = connected_transition[:index - 1]                   
                else:
                    array[line][column][0] = 0
                    array[line][column - 1][1] = 0
                    connected_transition.append(0)
                    connected.append([line, column - 1])
                    column -= 1