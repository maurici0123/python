def sorteia():
    num=[]

    print('sorteando numeros... ', end='')
    for c in range(0, 5):
        num.append(random.randint(0, 50))
        time.sleep(.5)
        print(f'{num[len(num)-1]} ', end='', flush='True')
    print('')
    time.sleep(1)
    return num

def somaPar(x):
    soma=0
    for c in x:
        if c%2==0:
            soma+=c
    print('-='*30)
    print(f'a soma dos números pares da lista {x} é: \033[32m{soma}\033[m')


############################
import random ,time
x=sorteia()
somaPar(x)