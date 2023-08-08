x = int(input('1º numero: '))
y = int(input('2º numero: '))
z = int(input('3º numero: '))

n = [x,y,z]
n.sort()

print('o menor numero é {}'.format(n[0]))
print('o maior numero é {}'.format(n[len(n)-1]))