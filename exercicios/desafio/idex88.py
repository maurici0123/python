import random
import time

tot_jogos=[]
jogo=[]

print('-'*18)
print('JOGO DA MEGA SENA')
print('-'*18)

quant=int(input('quantos jogos voçê quer que sorteie: '))

for c in range(1, quant+1):

    count=0
    while True:
        num = random.randint(1,60)
        if num not in jogo:
            jogo.append(num)
            count+=1
        if count == 6:
            break

    tot_jogos.append(jogo[:])
    jogo.clear()


print('-='*20)
for y, z in enumerate(tot_jogos):
    print(f'jogo {y+1}: {z}')
    time.sleep(.5)
print('-='*20)