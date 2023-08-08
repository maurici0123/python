name = input('\nqual seu nome completo: ')

aux = name.split()

print('seu nome em letra  maiuscula: {}'.format(name.upper()))
print('seu nome em letra minuscula: {}'.format(name.lower()))
print('quantidade de letras: {}'.format(len(name) - name.count(' ')))
print('quantidade de letras na primeira palavra: {}'.format(len(aux[0])))