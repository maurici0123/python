print('-'*22)
print('progressão aritmética')
print('-'*22)

option=1
while option!=2:
    s = int(input('\nprimeiro termo: '))
    p = int(input('razão: '))

    c=0
    while c<10:
        print(s, '→ ', end='')
        s+=p
        c+=1

    print('END')

    print('-'*10)
    print('[1] continuar')
    print('[2] sair')
    print('-'*10)
    option=int(input('opção: '))