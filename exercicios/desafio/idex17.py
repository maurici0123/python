import math

ca = float(input('digite o valor do cateto adjacente: '))
co = float(input('digite o valor do cateto oposto: '))

print('o valor da hipotenuza é {:.3f}'.format(math.sqrt(ca**2+co**2)))