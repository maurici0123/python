list=[]
impar=[]
par=[]

while True:
    n=int(input('digite um numero: '))
    list.append(n)

    if n%2==0:
        par.append(n)
    else:
        impar.append(n)
    
    option=input('voce quer continuar [S/N]: ').lower()
    if option=='n':
        break

print(f'\na lista: {list}')
print(f'a lista com os numeros pares: {par}')
print(f'a lsita com os numeros impares {impar}')