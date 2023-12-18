numbers=[[],[]]

for c in range(1,8):
    x=int(input(f'digite o {c}º numero: '))

    if x%2==0:
        numbers[0].append(x)
    else:
        numbers[1].append(x)

numbers[0].sort()
numbers[1].sort()
print('-'*25)
print(f'o numeros pares são {numbers[0]}')
print(f'o numeros impares são {numbers[1]}')