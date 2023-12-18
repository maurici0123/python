lista=[]

for c in range(1,6):
    n=int(input(f'digite o {c}º valor: '))

    if c==1:
        lista.append(n)
    else:

        for ind, count in enumerate(lista):
            if n < count:
               lista.insert(ind, n) 
               break

            if n > lista[len(lista)-1]:
                lista.append(n)
                break

print(f'\na lista: {lista}')