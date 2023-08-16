n1 = float(input('primeira nota: '))
n2 = float(input('segunda nota: '))

m = (n1+n2)/2

if m<5:
	print('voce esta reprovado')
elif m>=5 and m<7:
    print('voce esta de rrcuperaçao')
else:
    print('voce esta aprovado')