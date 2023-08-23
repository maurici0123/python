n = int(input('digite um numero inteiro: '))

a=0
for c in range(n, 0, -1):
	if n%c==0:
		a+=1
if a==2:
	print('o número {} é primo'.format(n))
else:
	print('o número {} é par'.format(n))