time=[]
jogador={
    'nome': '',
    'partidas': 0,
    'tot_gols': 0,
    'gols': []
}
gols=[]

while True:
    jogador.clear()
    gols.clear()
    jogador['nome']=input('nome do jogador: ')
    jogador['partidas']=int(input(f'quantas partidas o {jogador["nome"]} jogou: '))

    for x in range(1, jogador['partidas']+1):
        gols.append(int(input(f'quantos gols ele fez na {x}º partida: ')))
        jogador['gols']=gols[:]
        jogador['tot_gols']=sum(gols)
    
    time.append(jogador.copy())

    option=input('quer continuar [S/N]: ').lower()
    if option=='n':
        break

print('-='*20)
print(f'{"cod":>3}  {"nome":<10}{"jogos":<7}{"total":<7}{"gols"}')
print('-='*20)
for k, v in enumerate(time):
    print(f'{k:>3}  ', end='')
    print(f'{time[k]["nome"]:<10}', end='')
    print(f'{time[k]["partidas"]:<7}', end='')
    print(f'{time[k]["tot_gols"]:<7}', end='')
    print(f'{time[k]["gols"]}')
print('-='*20)

while True:
    option2=int(input('mostrar detalhes de cada jogador (999 sair): '))
    if option2==999:
        break
    if option2>=len(time) or option2<0:
        print(len(time))
        print('esse jogador não existe')
    else:
        print('-='*20)
        print(f'nome: {time[option2]["nome"]}')
        print(f'jogos: {time[option2]["partidas"]}')
        print(f'média de gols: {sum(time[option2]["gols"])/len(time[option2]["gols"]):.1f}')
        print(f'gols: {time[option2]["gols"]}')
        print(f'total de gols: {time[option2]["tot_gols"]}')