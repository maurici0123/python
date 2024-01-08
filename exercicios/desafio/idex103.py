def ficha(nome='<desconhecido>', gol=0):
    print('-'*40)
    print(f'o jogador {nome} fez {gol} gol(s) no campeonato')

print('-'*20)
nome=input('nome do jogador: ')
gol=input('quantos gol(s) o jogador fez: ')

if not gol.isnumeric():
    gol=0
if nome.strip()=='':
    ficha(gol=gol)
else:
    ficha(nome ,gol=gol)