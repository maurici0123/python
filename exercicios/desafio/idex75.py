par=0

n1=int(input('digite o 1º numero: '))
n2=int(input('digite o 2º numero: '))
n3=int(input('digite o 3º numero: '))
n4=int(input('digite o 4º numero: '))

tupla=(n1, n2, n3, n4)

print(f'\no numero 9 apareceu {tupla.count(9)} vezes')
if 3 in tupla:
    print(f'o numero tres esta na {tupla.index(3)+1}º posição')
else:
    print('o numero 3 nao aparece nenhuma vez')

for c in tupla:
    if c%2==0:
        par+=1
print(f'existem {par} numeros pares')