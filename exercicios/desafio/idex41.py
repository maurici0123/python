import datetime

nasc = int(input('em que ano voce nasceu: '))

ano = datetime.date.today().year
idade = nasc-ano

if idade <= 9:
    print('voce esta na categoria mirim')
elif idade <= 14:
    print('voce esta na categoria infantil')
elif idade <= 19:
    print('voce esta na categoria junior')
elif idade <= 25:
    print('voce esta na categoria sênior')
else:
    print('voce esta na categoria mastr')