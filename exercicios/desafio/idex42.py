l1 = float(input('1º lado: '))
l2 = float(input('2º lado: '))
l3 = float(input('3º lado: '))

if l1 > l2+l3 or l2 > l1+l3 or l3 > l2+l1:
    print('nao tem como formar um triangulo')
elif l1 == l2 and l2 == l3 and l3 == l1:
    print('com isso formara em triangulo equilátero')
elif l1 != l2 and l2 != l3 and l3 != l1:
    print('com isso formara em triangulo escaleno')
elif l1 or l2 and l2 or l3 and l3 or l1:
    print('com isso formara em triangulo isósceles')