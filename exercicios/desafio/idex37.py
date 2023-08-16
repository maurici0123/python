dec = int(input('digite um numero inteiro: '))

print('-'*35)
print('para qual base voce quer converter')
print('-'*35)
print(' [1] binario\n [2] octal\n [3] hexadecimal')
print('-'*35)
res = int(input())

if res == 1:
    print('{} em binario é: {}'.format(dec, bin(dec)[2:]))
elif res == 2:
    print('{} em octal é: {}'.format(dec, oct(dec)[2:]))
elif res == 3:
    print('{} em hexadecimal é: {}'.format(dec, hex(dec)[2:]))
else:
    print('e apenas 1, 2 ou 3')