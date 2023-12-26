def area(c, l):
    print('-='*10)
    print(f'a área de {c}x{l} do terreno é {c*l}m²')
    print('-='*10)

print('claculando a área')
print('-'*20)
x=float(input('LARGURA (m): '))
y=float(input('COMPRIMENTO (m): '))
area(x ,y)