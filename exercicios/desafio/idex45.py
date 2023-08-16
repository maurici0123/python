import random

option=0
while option != 2:
    print('-'*12)
    print('[1] pedra')
    print('[2] papel')
    print('[3] tesoura')
    print('-'*12)
    me = int (input('opção'))

    bot = random.randint(1,3)
    if bot == me:
        print('\033[4;33mempatou \033[m')
    elif bot == 1 and me == 2 or bot == 2 and me == 3 or bot == 3 and me == 1:
        print('\033[4;32mvenceu\033[m')
    elif me == 1 and bot == 2 or me == 2 and bot == 3 or me == 3 and bot == 1:
        print('\033[4;31mperdeu\033[m')
    
    print('-'*12)
    print('[1] continuar')
    print('[2] parar')
    print('-'*12)
    option = int (input('opção: '))
