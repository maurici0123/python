option=0

while option!=5:
    x=float(input('digite um numero: '))
    y=float(input('digite outro numero: '))
    option=0

    while option!=4 and option!=5:
        print('-'*20)
        print('[1] somar')
        print('[2] multiplicar')
        print('[3] o maior')
        print('[4] novos numeros')
        print('[5] sair')
        ('-'*20)
        option= int(input('opção: '))

        if option==1:
            print('a soma é {}'.format(x+y))
        elif option==2:
            print('a multiplicação é {}'.format(x*y))
        elif option==3:
            if x>y:
                print('o maior numero é {}'.format(x))
            elif y>x:
                print('o maior numero é {}'.format(y))
            else:
                print('os numeros soa iguais')