def contagem(s, e, p):

    print('-='*13)
    print(f'contagem de {s} até {e} de {abs(p)} em {abs(p)}')

    if s>e:
        for c in range(s, e-1, p):
            print(f'{c}', end=' ', flush='True')
            time.sleep(.5)
        print('FIM')
    else:
        for c in range(s, e+1, p):
            print(f'{c}', end=' ', flush='True')
            time.sleep(.5)
        print('FIM')

#############################################
import time

contagem(1 ,10, 1)
contagem(10 ,0, -2)

print('-='*13)
print('agora é sua vez')
s = int(input('digite o numero inicial: '))
e = int(input('digite o numero final: '))
p = int(input('digite o numero de passos: '))

contagem(s, e, p)