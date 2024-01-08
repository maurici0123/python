import mod

print('-'*20)
price=float(input('digite um preço: R$'))
print('-'*20)
print(f'o dobro de R${mod.moeda(price)} é R${mod.moeda(mod.dobro(price))}')
print('-'*20)
print(f'a metade de {mod.moeda(price)} é R${mod.moeda(mod.metade(price))}')
print('-'*20)
print(f'o aumento de 10% de R${mod.moeda(price)} è R${mod.moeda(mod.aumento(price))}')
print('-'*20)
print(f'a diminuição de 13% de R${mod.moeda(price)} é R${mod.moeda(mod.diminuição(price))}')
print('-'*20)