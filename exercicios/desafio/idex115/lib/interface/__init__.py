def line(tam):
    print('-'*tam)


def cabeçalho(te):
    line(42)
    print(f'\033[36m{te}\033[m'.center(42))
    line(42)


def leiaint(msg):
    while True:
        n=input(msg)
        if n.isnumeric():
            return int(n)
            break
        else:
            print('\033[31m[ERRO]\033[m digite um número inteiro')


def menu(list):
    cabeçalho('MENU PRINCIPAL')

    for k, v in enumerate(list):
        print(f'\033[36m{k+1}\033[m', '-', v)
    line(42)
    
    option = leiaint('sua opção: ')
    return option