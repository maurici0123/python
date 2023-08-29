import random
g=0
while True:
    print('-'*10)
    print('impar ou par')
    print('-'*10)
    print('[2] par')
    print('[1] impar')
    option=int(input('opção: '))
    n=int(input('quantos numeros: '))
    print("\n" * 8)

    cop=random.randint(1,2)
    s=n+cop
    
    if option==1:
        if s%2==0:
            print('voce perdeu')
            break
        else:
            print('voce ganhou')
            g+=1
    elif option==2:
        if s%2==0:
            print('voce ganhou')
            g+=1
        else:
            print('voce perdeu')
            break

print(f'voce ganho {g} seguidas')