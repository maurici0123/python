text = input('digite uma frase: ').lower()
print('a letra A aparece {} vezes'.format(text.count('a')))
print('a primeira letra A começa na posiçao {}'.format(text.find('a')+1))
print('a ultima letra A começa na posiçao {}'.format(text.rfind('a')+1))