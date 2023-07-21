import random

aluno1 = input('\nprimeiro aluno: ')
aluno2 = input('segundo aluno: ')
aluno3 = input('terceiro aluno: ')
aluno4 = input('quarto aluno: ')

sort = random.randint(1,4)

if sort == 1:
    print('a criança sorteada é {}'.format(aluno1))
if sort == 2:
    print('a criança sorteada é {}'.format(aluno2))
if sort == 3:
    print('a criança sorteada é {}'.format(aluno3))
if sort == 4:
    print('a criança sorteada é {}'.format(aluno4))