print('-'*18)
print('caixa eletronico')
print('-'*18)
cin=vin=dez=um=0

valor=int(input('valor a ser sacado: '))

while True:
    if valor >=50:
        valor-=50
        cin+=1
    else:
        break
while True:
    if valor >=20:
        valor-=20
        vin+=1
    else:
        break
while True:
    if valor >=10:
        valor-=10
        dez+=1
    else:
        break
while True:
    if valor >=1:
        valor-=1
        um+=1
    else:
        break

print(f'\ntotal de {cin} cédulas de 50')
print(f'total de {vin} cédulas de 20')
print(f'total de {dez} cédulas de 10')
print(f'total de {um} cédulas de 1')