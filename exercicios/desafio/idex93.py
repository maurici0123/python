jogador=dict()
gols=[]

jogador['nome']=input('nome do jogador: ')
jogador['partidas']=int(input(f'quantas partidas o {jogador["nome"]} jogou: '))

for x in range(1, jogador['partidas']+1):
    gols.append(int(input(f'quantos gols ele fez na {x}º partida: ')))
    jogador['gols']=gols
    jogador['tot_gols']=sum(gols)

print('-='*15)
print(f'total de partidas jogadas: {jogador["partidas"]}')
print(f'total de gols marcados: {jogador["tot_gols"]}')
print(f'total de gols marcados: {jogador["gols"]}')
print('-='*15)