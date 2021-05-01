from os import system

def processing_lst(lst):
    for i in range(len(lst)):
        res = lst[i]+"/"
        lst[i] = res
    return "".join(lst)

def clear():
    system('cls')

def cheak_message(message):
    if message == [] or message == [ ]:
        print("Нельзя шифровать пустое сообщение!")
        exit(0)

def cheak_key(n):
    ch_lst = list(range(1,33))
    if n not in ch_lst:
        clear()
        raise AssertionError("Недопустимый ключ!")

# Функция взлома шифра (без знания ключа):
def breaking_cipher(encrypt_message,alphabet):
    message = ""
    messages = {}
    const1 = 1
    const2 = 32
    index = 1
    for key in range(const1,const2+1):
        for i in encrypt_message:
            if (i in alphabet):      
                step = alphabet.index(i)
                message += (alphabet[(step - key) % len(alphabet)])
            else:
                message += (i)
        messages.update({key:message})
        index+=1
        message = ''
    print("Выберите из всех ниже приведённых строк 1 наиболее верную строку:")

    for i,e in enumerate(messages):
        print("{}: {}".format(e,list(messages.values())[i]))
    num = int(input("Введите номер: "))
    if num not in messages:
        print("Error: Данного номера не существует!")
        exit(0)
    print("Decrypted message: {}".format(messages.get(num).capitalize()))

def Decoding(e_m,key,alphabet):
    decrypted_message = ""
    for ind,step in enumerate(e_m):
        if (step in alphabet):      
            ind = alphabet.index(step)
            decrypted_message += alphabet[(ind - key) % len(alphabet)]
        else:
            decrypted_message += step

    # Запись расшифровки в файл:    
    with open("Encrypted_file.txt","a",encoding = "utf-8" ) as f:
        f.write("\nYou decrypted message:\n{}".format(decrypted_message.capitalize()))
    # Вывод расшифрованного сообщения:
    print("Decrypted message: {}".format(decrypted_message.capitalize()))

def Encrypt(message):
    cheak_message(message)
    alphabet = list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
    message = list(processing_lst(message))
    key = int(input("Enter a key in the range from 1 to 32: "))
    cheak_key(key)
    encrypt_message = ""
    for ind,step in enumerate(message):
        if (step in alphabet):      
            ind = alphabet.index(step)
            encrypt_message += alphabet[(ind + key) % len(alphabet)]
        elif step == '/':
            encrypt_message += " "
        else:
            encrypt_message += step
    # Запись в файл:        
    with open("Encrypted_file.txt","w",encoding = 'utf-8') as f:
        f.write("You encrypted message:\nCipher: {}".format(encrypt_message.capitalize()))
    # Вывод:
    print("Encrypt message: {}".format(encrypt_message.capitalize()))
    what(encrypt_message,key,alphabet)

def what(encrypt_message,key,alpha):
    # функция взаимодействия с пользователем:
    choice = input("Decode the message(y or n): ").lower()
    if choice == 'y':
        clear()
        key2 = int(input("Enter the previously entered key: "))
        if key2 != key:
            print("Неверный ключ расшифровки!")
            choice = input("Попробовать взломать сообщение - {}(yes or no): ".format(encrypt_message)).lower()
            if choice == "yes":
                breaking_cipher(encrypt_message,alpha)
            else:
                exit(0)   
        else:
            Decoding(encrypt_message,key2,alpha)
    elif choice == 'n':
        print('Exit!')
        exit(0)
    else:
        clear()
        raise AssertionError("Неизвестная команда!")

Encrypt(message = input("Enter a message: ").lower().split())    
