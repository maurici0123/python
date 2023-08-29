while True:
	print('-'*10)
	print('tabuada: ')
	print('-'*10)
	n=int(input('numero: '))
	
	if n<=0:
		break
	else:
		for c in range(1,11):
			print('{} X {} = {}'.format(n, c, n*c))