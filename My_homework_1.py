# -*- coding: utf8 -*-     
def main():
    import time,os
    #задача номер 1:
    clear = lambda:os.system("cls")
    def translation_if_int(inp):
        if inp.is_integer():
            inp = int(inp)
            return inp
        else:
            return inp
    def Time(t):
        time.sleep(t)
    def task_1():# №1
        clear()
        print("Task_1:")
        Time(1.5)
        clear()
        try:
            a = float(input("Введите любое число:\n"))
        except Exception as e:
            print("Ошибка: {}.".format(e))
            exit(0)
        a = translation_if_int(a)
        clear()
        try:
            b = float(input("Введите ещё одно любое число:\n"))
        except Exception as e :
            print("Ошибка: {}.".format(e))
            exit(0)
        b = translation_if_int(b)
        clear()
        amount = a + b
        diference = a - b
        composition = a * b             
        print("Сумма чисел {0} и {1} = {2}.\nРазность чисел {0} и {1} = {3}.\nПроизведение чисел {0} и {1} = {4}.".format(a,b,amount,diference,composition))
        Time(5)
    #задача номер 2
    def task_2():# №3
        clear()
        print("Task_2:")
        Time(1.5)
        clear()
        try:
            cube_edge_len = float(input("Введите длинну ребра куба:\n"))
        except ValueError as e:
            print("Ошибка: {}\nВведите 'действительное' число!.".format(e))
            exit(0)
        cube_edge_len = translation_if_int(cube_edge_len)
        # все стороны квадрата равны и все рёбра куба равны.
        # длинна ребра в 3 степени = V(куба)
        V_cub = cube_edge_len**3# Обьём куба.
        # длинна ребра в 2 степени * на 4(т.к "боковых" поверхностей у куба всего - 4 )= S(б.п).
        S_cube_surface = ((cube_edge_len**2)*4) # площадь боковой повехности куба
        clear()
        print("Обьём куба: {}.\nПлощадь боковой поверхноси куба: {}.".format(V_cub,S_cube_surface))
        Time(5)
    # задача номер 3
    def task_3():# №31
        clear()
        print("Task_3:")
        Time(1.5)
        clear()
        try:
            a = float(input('Введите число которое хотите возвести в степень:\n'))
        except Exception as e:
            print("Ошибка: {}\nВведите 'действительное' число!.".format(e))
            exit(0)
        clear()
        a = translation_if_int(a)
        print("Ваши числа:")
        #за  2 операции:
        a2 = a * a
        a4 = a2 * a2
        print("{}**4 = {}".format(a,a4))
        #за 3 операции:
        a2 = a * a
        a4 = a2 * a2
        a6 = a4 * a2
        print("{}**6 = {}".format(a,a6))
        #за 4 операции:
        a2 = a * a
        a3 = a2 * a
        a4 = a2 * a2
        a7 = a4 * a3
        print("{}**7 = {}".format(a,a7))
        #за 3 операции:
        a2 = a * a
        a4 = a2 * a2
        a8 = a4 * a4
        print("{}**8 = {}".format(a,a8))
        #за 4 операции:
        a2 = a * a
        a4 = a2 * a2
        a8 = a4 * a4
        a9 = a8 * a
        print("{}**9 = {}".format(a,a9))
        #за 4 операции:
        a2 = a * a
        a4 = a2 * a2
        a8 = a4 * a4
        a10 = a8 * a2
        print("{}**10 = {}".format(a,a10))
        #за 5 операции:
        a2 = a * a
        a4 = a2 * a2
        a5 = a4 * a
        a8 = a4 * a4
        a13 = a8 * a5
        print("{}**13 = {}".format(a,a13))
        #за 5 операции:
        a2 = a * a
        a3 = a2 * a
        a6 = a3 * a3
        a12 = a6 * a6
        a15 = a12 * a3
        print("{}**15 = {}".format(a,a15))
        #за 6 операции:
        a2 = a * a
        a3 = a2 * a
        a6 = a3 * a3
        a7 = a6 * a
        a14 = a7 * a7
        a21 = a14 * a7
        print("{}**21 = {}".format(a,a21))
        #за 6 операции:
        a2 = a * a
        a4 = a2 * a2
        a8 = a4 * a4
        a12 = a8 * a4
        a16 = a8 * a8
        a28 = a16 * a12
        print("{}**28 = {}".format(a,a28))
        #за 6 операции:
        a2 = a * a
        a4 = a2 * a2
        a8 = a4 * a4
        a16 = a8 * a8
        a32 = a16 * a16
        a64 = a32 * a32
        print("{}**64 = {}".format(a,a64))
    return task_1,task_2,task_3
#Кладём в переменные функции содержащиеся в main().
task_1,task_2,task_3 = main()
#вызываем по порядку:
task_1()

task_2()

task_3()

