distancia = int(input('qual a distancia em km: '))

if distancia <= 200:
    print('o valor da passagem é de R${:.2f}'.format(distancia*0.5))
else:
    print('o vaor da passagem é de R${:.2f}'.format(distancia*0.45))