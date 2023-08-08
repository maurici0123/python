l1 = float(input('1º lado: '))
l2 = float(input('2º lado: '))
l3 = float(input('3º lado: '))

if l1 > l2+l3 or l2 > l1+l3 or l3 > l2+l1:
    print('nao tem como formar um triangulo')
else:
    print('tem como formar um triangulo')