name = input('digite o seu nome inteiro: ')
print('a primeira palavra é {}'.format(name.split()[0]))
print('a ultima palavra é {}'.format(name.split()[len(name.split())-1]))