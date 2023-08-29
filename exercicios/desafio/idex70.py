print('-'*8)
print('compras')
print('-'*8)

tot=c=aux=mil=barato=0

while True:
    name= input('nome do produto: ')
    price=int(input('preço do produto: '))
    c+=1

    tot+=price
    if c==1:
        brato=name
        aux=price
    elif price<aux:
        barato=name

    if price>1000:
        mil+=1

    option=input('quer continuar [s/n]: ').lower()
    if option=='n':
        break

print(f'\no total gasto foi {tot}')
print(f'tem {mil} produtos acima de mail reais')
print(f'o produto mais barato é o {barato}')