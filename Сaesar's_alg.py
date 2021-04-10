from os import system

def processing_lst(lst):
    for i in range(len(lst)):
        res = lst[i]+"/"
        lst[i] = res
    return "".join(lst)

def clear():
    system('cls')

def cheak_num(n):
    ch_lst = list(range(-32,33))
    ch_lst.pop(32)
    print(ch_lst)
    if n not in ch_lst:
        clear()
        raise AssertionError("Недопустимый ключ!")

def Decoding(e_m,key,alphabet):
    decrypted_message = ""
    for ind,step in enumerate(e_m):
        if (step in alphabet):      
            ind = alphabet.index(step)
            decrypted_message += alphabet[(ind - key) % len(alphabet)]
        elif step == '/':
            decrypted_message += " "
        else:
            decrypted_message += step
    print("Decrypted message: {}".format(decrypted_message.capitalize()))

def Encrypt():
    alphabet = list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
    message = input("Enter a message: ").lower().split()
    message = list(processing_lst(message))
    key = int(input("Enter a key in the range from -32 to 32: "))
    cheak_num(key)
    encrypt_message = ""
    for ind,step in enumerate(message):
        if (step in alphabet):      
            ind = alphabet.index(step)
            encrypt_message += alphabet[(ind + key) % len(alphabet)]
        elif step == '/':
            encrypt_message += " "
        else:
            encrypt_message += step
    print("Encrypt message: {}".format(encrypt_message.capitalize()))
    choice = input("Decode the message(y or n): ").lower()
    if choice == 'y':
        key2 = int(input("Enter the previously entered key: "))
        if key2 != key:
           exit(0)
        else:
            Decoding(encrypt_message,key2,alphabet)
    elif choice == 'n':
        exit(0)
    else:
        clear()
        raise AssertionError("Неизвестная команда!")
Encrypt()    