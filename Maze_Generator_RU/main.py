import random
import time
import labirint_generation as gen
import Game_play as game
import auto_run
import graphics as gr
import graph

def main():
    print("Введите номер выбранного алгоритма из списка")
    print("1) Алгоритм Уинстона (Сложность: высокая Скорость: высокая)")
    print("2) Алгоритм Олдоса - Бродера (Сложность: высокая Скорость: маленькая)")
    print("3) Алгоритм Остовного дерева (Сложность: низкая Скорость: высокая)")
    print("4) Алгоритм Обхода в глубину (Сложность: высокая Скорость: высокая) !только для лабиринтов размера <= 40 * 40")
    algorithm_name = int(input())
    print("Введите желаемый размер")
    size = int(input())
    print("Введите желаемый режим")
    print("1) игра")
    print("2) автопрохождение")
    tipe = int(input())
    array = []
    gen.CreateArray(array, size)
    if algorithm_name == 4:
        array_color = []
        gen.CreateArrayUse(size, array_color)
        gen.DFS(array, size, 0, 0, array_color)
    elif algorithm_name == 2:
        array_color = []
        gen.CreateArrayUse(size, array_color)
        gen.OldasAlgoritm(array, size, 0, 0, array_color, 0)
    elif algorithm_name == 3:
        gen.OstovTree(array, size)
    else:
        array_not_use = []
        gen.CreateArrayNotUse(size, array_not_use)
        array_color = []
        gen.CreateArrayUse(size, array_color)
        gen.Uinston(array, size, array_not_use, array_color)
    window = gr.GraphWin("Лабиринт", 720, 720)
    window.setBackground("white")
    graph.PrintLabirint(array, size, 600 // size, window)
    if tipe == 1:
        game.Game(array, size, 600 // size, window)
    else:
        auto_run.GoLabirint2(array, size, 0, 0, 600 // size, window)
        time.sleep(3)
        window.close()

main()