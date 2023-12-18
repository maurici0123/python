dados = []
pessoa = []
count=0

while True :

    pessoa.append(input('nome da pessoa: '))
    pessoa.append(int(input('peso da pessoa: ')))
    dados.append(pessoa[:])
    pessoa.clear()

    if len(dados)==1:
        pesoma=dados[0][1]
        pesome=dados[0][1]

    if dados[count][1]>pesoma:
        pesoma=dados[count][1]
    if dados[count][1]<pesome:
        pesome=dados[count][1]
    count+=1

    op = input('quer continuar ? ').lower()
    if op=='n':
        break

print('-'*26)
print(f'foram registrados {len(dados)} pessoas')
print(f'a pessoa mais pesada tem {pesoma}Kg')
print(f'a pessoa mais leve tem {pesome}Kg')