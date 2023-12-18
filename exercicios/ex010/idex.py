lanche=('suco', 'panqueca', 'pao', 'cachorro quente', 'refri')

# for c in lanche:
#     print(c)
# print('')

# for c in range(0, len(lanche)):
#     print(lanche[c], c)
# print('')

for c, comida in enumerate(lanche):
    print(comida, c)

num=(4, 8, 1, 5, 9, 5, 7, 3, 4, 3)

print(sorted(num))
print(num.index(3))
del(num)