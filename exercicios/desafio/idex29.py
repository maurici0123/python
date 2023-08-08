v = float(input('qual a velocida de do carro: '))

if v <= 80:
    print('continua assim :)')
else:
    multa = (v-80)*7
    print('voce tomou uma multa de R${:.2f}'.format(multa))