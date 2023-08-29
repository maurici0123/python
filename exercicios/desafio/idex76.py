lista=('lapis',0.50, 'caderno',55.90, 'mochila',110.90, 'caneta',1.00, 'cartolina',1.20, 'borracha',2.50)


print('-'*20)
print(' lista de produtos')
print('-'*20)
for c in range(0, len(lista)):
    if c%2==0:
        print(f'{lista[c]:.<20}', end=' ')
    else:
        print(f'R$ {lista[c]:.2f}')