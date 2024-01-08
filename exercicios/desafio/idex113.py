
while True:
    try:
        i=int(input('digite um número inteiro: '))
    except:
        print('\033[31m[ERRO] digite um número inteiro\033[m')
    else:
        break
print('='*20)
while True:
    try:
        f=float(input('digite um número real: '))
    except:
        print('\033[31m[ERRO] digite um número real\033[m')
    else:
        break

print(f'o valor inteiro digitado foi {i} e o real foi {f}')