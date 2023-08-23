peso=[]
for c in range(0,5):
    peso.append(int(input('digite o peso da {}º pessoa: '.format(c+1))))

peso.sort()
print('\no maior peso lido foi {}'.format(peso[len(peso)-1]))
print('o menor peso lido foi {}'.format(peso[0]))