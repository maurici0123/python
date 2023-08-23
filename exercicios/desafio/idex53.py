text = input('escreva uma frase: ')
text = text.replace(' ','')

c = len(text)-1
pali=[]
while c >= 0:
    pali.append(text[c])
    c-=1
pali = ''.join(pali)

if text == pali:
    print('a frase é um palíndrmo')
else:
    print('a frase não é um palíndromo')