salario = float(input('qual o valor do salario do funcionario: '))

if salario > 1250:
    print('o novo salario do funcionario é {}'.format(salario*1.1))
else:
    print('o novo salario do funcionario é {}'.format(salario*1.15))