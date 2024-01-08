def leiaint(p):
    n=input(p)
    if n.isnumeric():
        return n
    else:
        print('\033[31m[ERRO]\033[m digite um número inteiro')

number=leiaint('digite um número: ')
print(f'voce digitou o número \033[32m{number}\033[m')