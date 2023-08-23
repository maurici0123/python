import datetime

mai=0
men=0
ano = datetime.date.today().year
for c in range(0, 7):
    x = int(input('ano de nacimento da {}º pesooa: '.format(c+1)))
    if ano-x >=18:
        mai += 1
    else:
        men += 1

print('\ntem {} pessoa(s) maior de idade'.format(mai))
print('tem {} pessoa(s) menor de idade'.format(men))