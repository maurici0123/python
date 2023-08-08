import random

print('\nvoce tem que adivinhar um numero de um a cinco')
x = int(input('digite um numero de [1:5]: '))

r = random.randint(1,5)

if x == r:
    print('voce acertou!')
if x != r:
    print('voce errou')
    print('o numero era ', r)