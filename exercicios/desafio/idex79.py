number=[]
while True:
    n=int(input('digite un numero: '))

    if n in number:
        print('voce ja digitou este numero')
    else:
        number.append(n)
    
    option=input('voce quer continuar [S/N]: ').lower()
    if option=='n':
        break

number.sort()
print(f'\nsua lista em ordem crescente: {number}')