import datetime

nasc = int(input('em que ano voce nasceu: '))

ano = datetime.date.today().year
idade = ano-nasc

if idade == 18:
    print('voce tem que se alistar no exército esse ano')
elif idade < 18:
    print('\nvoce ainda vai se alistar\nfalta {} anos(s)'.format(18-idade))
else:
    print('\nvoce passou do tempo de se alistar\npassou {} anos(s) do prazo'.format(idade-18))
