def maior(num):
    m=num[0]
    for c in num:
        if c>m:
            m=c
    print('-'*30)
    print(f'o maior número da lista é {m}')
    print('-'*30)

n=[]
print('-'*15)
print('o maior número')
print('-'*15)
x=int(input('quntos números voce quer analisar: '))

for c in range(0, x):
    n.append(int(input(f'digite o {c+1}º número: ')))

maior(n)