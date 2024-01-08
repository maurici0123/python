import mod

print('-'*20)
price=float(input('digite um preço: R$'))
print('-'*20)
print(f'a metade de {price} é {mod.metade(price)}')
print('-'*20)
print(f'o dobro de {price} é {mod.dobro(price)}')
print('-'*20)
print(f'o aumento de 10% de {price} è {mod.aumento(price)}')
print('-'*20)
print(f'a diminuição de 13% de {price} é {mod.diminuição(price)}')
print('-'*20)