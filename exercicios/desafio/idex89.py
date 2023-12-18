dados=[]
aluno=[]

while True:
    aluno.append(input('nome do aluno(a): '))
    aluno.append(float(input('primeira nota: ')))
    aluno.append(float(input('segunda nota: ')))

    dados.append(aluno[:])
    aluno.clear()

    option=input('quer continuar: ').lower()
    if option=='n':
        break
    print('-'*20)

print('-='*15)
print(f'{"Nº":<5}{"NOME":<18}NOTA')
print('-='*15)

for x, y in enumerate(dados):
    print(f'{x:<5}{dados[x][0]:<18}{(dados[x][1]+dados[x][2])/2:.1f}')

print('-='*15)

while True:
    option=int(input('mostrar notas de qual aluno? (999 interrompe): '))
    if option==999:
        break
    print(f'as notas de {dados[option][0]} são {dados[option][1],dados[option][2]}')
    print('-'*30)