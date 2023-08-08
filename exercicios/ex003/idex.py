text = 'nao adentre a boa noite apenas com ternura'

text2 = '  a velhice quiema e clama ao cair do dia  '

print(text[5])
print(text[4:17])
print(text[4:40:2])
print(text[:15])
print(text[4:])
print(text[0::2])
print(text[:16:2])

print(len(text)) # comprimento da string
print(text.count('a')) # qunatidade que tem a letra a
print(text.count('o',3,43))# qunatidade que tem a letra o da 3º ate a 43º
print(text.find('boa')) # posiçao que começa o parametro
print(text.find('furia')) # posiçao que começa o parametro
print('ternura' in text) # se tem ou nao o parametro
print(text.replace('adentre', 'entre')) # troca uma string pela outra
print(text.upper()) # deixa em caps lock
print(text.lower()) # deixa com letra minuscula
print(text.capitalize()) # deixa a primera letra da string em caps lock
print(text.title()) # deixa a primera letra de toda palavra em caps lock

print(text2.strip()) # tira os espaços no começo e final da string
print(text2.rstrip()) # tira os espaços no final da string
print(text2.lstrip()) # tira os espaços no começo da string

aux = text.split() # transfoma a string e array 
print(aux)
print(text.split()[5])
print(' # '.join(aux)) # junta os indices do array e separa por um parametro