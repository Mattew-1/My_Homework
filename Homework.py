def tack():
    # Таблица умножения от 2 до 9:

    tabl = ['{} {} * {} = {}\t{}'.format('Таблица умножения:\n\n' if t == 2 and ind == 1 else '',\
    t, ind, t*ind, '\n'*2 if ind == 10 and t == 5 else '') for t in range(2, 10) for ind in range(1, 11)]
    for index in range(20): print(tabl[index] + tabl[index + 10] + tabl[index + 20]  + tabl[index + 30]) if index < 10 else \
        print(tabl[index + 30]  + tabl[index + 40]  + tabl[index + 50]  + tabl[index + 60])

    #full version:
    '''tabl = []
    for t in range(2, 10):
        for ind in range(1, 11):
            tabl.append('{} * {} = {}\t'.format(t, ind, t * ind))
                    
    for  index i n range(20):
        if index < 10:
            print(tabl[index] + tabl[index + 10] + tabl[index + 20]  + tabl[index + 30])      

        else:
            print(tabl[index + 30]  + tabl[index + 40]  + tabl[index + 50]  + tabl[index + 60]) 
        
        if index == 9:
            print('\n'*2)'''

def tack2():
    from random import randint

    k = randint(1, 16)
    for i in range(k):
        print('#' * (randint(0, 10)))

tack()
#tack2()