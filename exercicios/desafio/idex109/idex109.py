import mod

print('-'*20)
price=float(input('digite um preço: R$'))
print('-'*20)
print(f'o dobro de R${mod.moeda(price)} é R${mod.dobro(price)}')
print('-'*20)
print(f'a metade de {mod.moeda(price)} é R${mod.metade(price, False)}')
print('-'*20)
print(f'o aumento de 10% de R${mod.moeda(price)} è R${mod.aumento(price)}')
print('-'*20)
print(f'a diminuição de 13% de R${mod.moeda(price)} é R${mod.diminuição(price, False)}')
print('-'*20)