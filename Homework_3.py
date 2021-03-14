from os import system
from time import sleep
# assert и задаваемые параметры в функциях в принципе не требуются в таком виде, как у меня и никак не используются в программе, но они есть просто так, навсякий случай.

def my_min(a = None,b = None,c = None,cheak = None):
# Только для чисел.
# Может принимать в себя 2 или 3 значения.(В соответствии с задачей)
# Функция получения наименьшего значения:

    assert a != None and b != None ,("Error: не были переданы аргументы!")
    assert cheak == None,("Было передано больше 3 аргументов!")
    # Проверка на наличие 'чужеродного обьекта' - строки:
    assert (not isinstance(a,str) and not isinstance(b,str) and not isinstance(c,str)),("Была переданна строка!")
    if c == None:
        if a > b:
            return b
        else:
            return a
    else:
        if a > b:
            res = b
        else:
            res = a
        if res > c:
            return c
        else:
            return res

def my_max(a = None,b = None,c = None,cheak = None):
# Только для чисел.
# Может принимать в себя только 2 или 3 значения.(В соответствии с задачей)
# Функция получения нaибольшего значения:

    assert a != None and b != None ,("Error: не были переданы аргументы!")
    assert cheak == None,("Было передано больше 3 аргументов!")
    # Проверка на наличие 'чужеродного обьекта' - строки:
    assert (not isinstance(a,str) and not isinstance(b,str) and not isinstance(c,str)),("Была переданна строка!")
    if c == None:
        if a > b:
            return a
        else:
            return b
    else:
        if a > b:
            res = a
        else:
            res = b
        if res > c:
            return res
        else:
            return c


def clear():
    system("cls")

def task_1(): # №33
    clear()
    print("task №33:")
    try:
        x = float(input("Введите любое число: "))
    except Exception:
        raise TabError("Недопустимый ввод!")
    clear()
    try:
        y = float(input("Введите любое число: "))
    except Exception:
        raise TabError("Недопустимый ввод!")
    clear()
    max_num = my_max(x,y)
    min_num = my_min(x,y)
    print("Наибольшие из {} и {} это - {}".format(x,y,max_num))
    print("Наименьшие из {} и {} это - {}".format(x,y,min_num))
    sleep(8)
def task_2(): # №34
    print("task №34:")
    sleep(1.6)
    clear()
    try:
        x = float(input("Введите любое число:"))
    except Exception:
        raise TabError("Недопустимый ввод!")
    clear()
    try:
        y = float(input("Введите любое число:"))
    except Exception:
        raise TabError("Недопустимый ввод!")
    clear()
    try:
        z = float(input("Введите любое число:"))
    except Exception:
        raise TabError("Недопустимый ввод!")
    clear()
    max_num = my_max(x,y,z)
    min_num = my_min(x,y,z)
    print("Наибольшие из {}, {} и {} это - {}".format(x,y,z,max_num))
    print("Наименьшие из {}, {} и {} это - {}".format(x,y,z,min_num))
    sleep(8)
def task_3():#№35
    print("task №35:")
    sleep(1.6)
    clear()
    try:
        x = float(input("Введите любое число: "))
    except Exception:
        raise TabError("Недопустимый ввод!")
    clear()
    try:
        y = float(input("Введите любое число: "))
    except Exception:
        raise TabError("Недопустимый ввод!")
    clear()
    try:
        z = float(input("Введите любое число: "))
    except Exception:
        raise TabError("Недопустимый ввод!")
    clear()
    max_num = my_max(x+y+z,x*y*z)
    min_num = (my_min(x+y+z/2,x*y*z)**2)
    min_num = min_num + 1
    print("max -",str(max_num))
    print("min -",str(min_num))
    sleep(8)
def meny():
    #номера  в соответствии с заданием.
    # нажать на 1 чтоб получить всё сразу.
    # нажать на 0 чтоб выйти.
    while True:
        clear()
        what = input("Введите номер задания: ")
        what  = what.split()
        what = "".join(what)
        if what == '33' or what == '№33':
            task_1()
        elif what == '34' or what == '№34':
            task_2()
        elif what == '35' or what == '№35':
            task_3()
        elif what == '1':
            task_1()
            sleep(1)
            task_2()
            sleep(1)
            task_3()
            sleep(1)
        elif what == '0':
            clear()
            break
        else:
            print("Данного номера нет в списке.\nПовторите попытку.")
            sleep(3)
# Вызов:
meny()
