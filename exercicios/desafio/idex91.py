import time, random, operator
dados=dict()
ranking={}
for x in range(1,5):
    time.sleep(.5)
    y=random.randint(1,6)
    dados["jogador {}".format(x)]=y
    print(f'o {x}º jogador tirou \033[35m{y}\033[m')

print('-='*16)
print('ranking dos jogadores')
print('-='*16)

ranking= sorted(dados.items(), key=operator.itemgetter(1), reverse=True)
for x in range(0,4):
    #print(ranking)
    print(f'{x+1}º lugar: {ranking[x][0]} que tirou {ranking[x][1]}')

print('-='*16)