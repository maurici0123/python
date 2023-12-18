number=[]
pos_ma=[]
pos_me=[]
for c in range(1,6):
    number.append(int(input(f'digite o {c}º numero: ')))

    if c==1:
        maior=number[0]
        pos_ma.append(0)

        menor=number[0]
        pos_me.append(0)
    else:

        if number[len(number)-1]==menor:
            pos_me.append(len(number)-1)

        elif number[len(number)-1]<menor:
            menor=number[len(number)-1]
            pos_me.clear()
            pos_me.append(len(number)-1)
        
        if number[len(number)-1]==maior:
            pos_ma.append(len(number)-1)

        elif number[len(number)-1]>maior:
            maior=number[len(number)-1]
            pos_ma.clear()
            pos_ma.append(len(number)-1)

print('-'*10)
print(f'sua lista foi {number}')
print(f'\no maior numero foi {maior} na posição {pos_ma}')
print(f'o menor numero foi {menor} na posição {pos_me}')