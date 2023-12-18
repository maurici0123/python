number=[]
while True:
    n=int(input('digite un numero: '))

    number.append(n)
    
    option=input('voce quer continuar [S/N]: ').lower()
    if option=='n':
        break

print(f'\nquantidade de numero na lista: {len(number)}')

number.sort(reverse=True)
print(f'\nlista em ordem decrescente: {number}')

if 5 in number:print('\no numero 5 foi digitado an lista')
else: print('\no numero 5 nao foi digitado an lista')