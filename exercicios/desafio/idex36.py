casa = float(input('quanto custa a casa: '))
salario = float(input('quanto voce ganha por mes: '))
anos = int(input('em quantos anos voce pretende pagar a casa: '))


if casa/anos > salario*0.3:
    print('voce nao pode financiar esta casa')
else:
    print('voce pode financiar esta casa :)')