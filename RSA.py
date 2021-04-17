
# Шифрование алгоритм RSA:

from random import choice, randint
# Создание списка простых чисел до задданного числа:
def create_num(n):
    '''if n < 2:
        return '''
    max_ndx = (n - 1) // 2
    lst = [True] * (max_ndx + 1) # создание списка чисел до n,(все числа это True)
    for ndx in range(int(n ** 0.5) // 2):
        if lst[ndx]:
            num = ndx * 2 + 3# формула помогающая определить простое число
            lst[ndx+num:max_ndx:num] = [False] * ((max_ndx-ndx-num-1)//num + 1)# затирание обычных чисел нулями(простые - True, непростые - False  )
    return [2] + [ndx * 2 + 3 for ndx in range(max_ndx) if lst[ndx]] # возвращение списка простых чисел(непростые числа отсеиваются.)

# Функция проверки сообщения(p.s Во избежение потери точности):
def cheak(m,key):
    if len(str(m)) >= len(str(key)):# Если передаваемое сообщение больше ключа: сгенерировать ошибку.
        print("Error: слишком большое сообщение.")
        exit(0)

# Проверка сообщения на наличие символов отличных от цифр и проверка на пустоту сообщения:
def cheak_mess(mes):
    if mes == '':
        raise AssertionError("Нельзя шифровать пустое сообщение!")
    return mes.isdigit()# return True or False

# проверка 2х простых чисел на уникальность:
def cheak_num(num1,num2):
    if num1 == num2:
        while num1 == num2:
            print("Error: 202")
            res = create_num(25000000)   
            num1 = res[(len(res) - randint(10000,30000))]
    return num1,num2 

''' Основная функция шифровки сообщения.
    Генерация ключа и шифрование передаваемого сообщения.'''
def Encrypt(message, n = 40000000):
    # список чисел от 1 до n:
    lst_num = list(range(1,30000))
    # кладём наш список простых чисел в переменную:
    lst_whole = create_num(n)
    l = len(lst_whole)   
    num = int(l-(l/100*17))   
    # случайный выбор простых чисел
    a = choice(lst_whole[num:])
    b = choice(lst_whole[num:])
    # проверка a and b на уникальность:
    a,b = cheak_num(a,b)
    # создание открытого ключа:
    public_key = a * b
    # Проверка:
    cheak(message,public_key)
    # число фи:
    f = ((a-1)*(b-1))
    # генерация открытой экспоненты;
    i = 0
    while True:
        step = lst_whole[i]
        if (f % step != 0):# получаем такое значение step чтоб при делении на f было не целое число.
            e = step
            break
        else:
            i+=1
    i = 0
    # Получение секретной экспоненты:
    while True:
        step = lst_num[i]
        res = (f*step+1)/e
        if res.is_integer():# получаем целое число res.
            secret_e = int(res)
            break
        else:
            i+=1
    # шифрование: возводим сообщение в степень открытой экспоненты и делим по модулю на открытый ключ.
    encrypted_message = pow(message,e,public_key)
    return encrypted_message,secret_e,public_key

# функция получения букв из значений(юникод)
def get_let(lst):
    decrypted_message = ''
    for i in lst:
        decrypted_message += chr(i)
    return "".join(str(e) for e in decrypted_message)

# Функция расшифровки шифрованного сообщения:     
def Decrypt(en_m,keys,designation):
    # определение типа сообщения(num or let)
    if designation == "int":
        # вывод расшифрованного сообщения.
        print("Decrypted message: {}".format(pow(en_m, list(keys.keys())[0], list(keys.values())[0] ) ) )
    else:
        result = []
        for ind in range(len(en_m)):
            res = pow(en_m[ind], list(keys.keys())[ind], list(keys.values())[ind])
            result.append(res)
        decrypted_message = get_let(result)
        # вывод расшифрованного сообщения.
        print("Decrypted message: {}".format(decrypted_message))

# Главная функция:
def main(message):
    if cheak_mess(message):
        message = int(message)
        keys = {}
        encrypted_message,e,k = Encrypt(message)
        keys.update({e: k})
        # вывод:
        print("\nYour encrypted message:", encrypted_message)
        print("\nPublic key:", list(keys.values())[0])
        # запрос на то что сделать?
        choice = input("Decrypt the message: ").lower()
        if choice ==  "yes":
            Decrypt(encrypted_message,keys,designation = "int" )
        else:
            exit(0)
    else:
        message = list(message)
        alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890,.!?+/*@#$&№%;:()-=_"
        keys = {}
        encrypted_message = []
        # проходимся по сообщеннию заменяя каждый символ цифрами:
        for iters,element in enumerate(message):
            if element in alphabet:
                message[iters] = ord(element) # получение чисел соответсвующих им символов по таблице юникод.
            else:
                print("ERROR: Неверный символ!")
                print(element,"- нельзя шифровать.")
                exit(0)
        # передача в функцию шифровки по 1 символу:
        for i in message:
            m,e,k = Encrypt(i,10000000)
            encrypted_message.append(m)
            keys.update({e: k})

        #вывод:
        print("\nYour encrypted message:", ", ".join(str(e) for e in encrypted_message))
        print("\nPublic keys: {}".format(", ".join(str(e) for e in list(keys.values()))))

        # запрос на то что сделать?
        choice = input("\nDecrypt the message(yes or no): ").lower()
        if choice ==  "yes":
            Decrypt(encrypted_message,keys,designation = "str")
        else:
            exit(0)
main(message = input("Enter message: "))
