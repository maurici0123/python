list=[4, 8, 1, 5, 0, 4, 7, 1, 3, 8, 3]

# list_b = list /ligação 
# list_b = list[:] /copia

print(list)

print(list.count(4)) # quantas vezes aparece na lista

list.append(9) # insere o numero 9 no ultimo indice
print(list)

list.insert(0, 3) # insere o numero 3 no indice 0
print(list)

list.pop() # remove o ultimo indice 
print(list)
list.pop(0) # remove o indice 0
print(list)

list.remove(1) # remove o numero 1
print(list)

# del(list) remove a lista
del(list[1]) # remove o indice 1
print(list)

list.sort(reverse=True) # ordem decrescente
print(list)
list.sort() # ordem crescente
print(list)

list.clear() # limpa a lista
print(list)