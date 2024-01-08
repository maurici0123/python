from lib import interface, arquivo
from time import sleep

arq = 'pessoas.txt'

# if not arquivo.arquivoExiste(arq):
#     arquivo.criarArquivo(arq)


while True:
    res = interface.menu(['ver pessoas cadastradas', 'cadastrar nova pessoa', 'sair do sistema'])

    if res == 1:
        arquivo.lerArquivo(arq)
        sleep(.5)
    elif res == 2:
        interface.cabeçalho('NOVO CADASTRO')
        nome = str(input('nome: '))
        idade = interface.leiaint('idade: ')
        arquivo.cadastrar(arq, nome, idade)
    elif res == 3:
        interface.cabeçalho('saindo do sistema')
        break
    else:
        print('\033[31m[ERRO]\033[m digite um número válido')
        sleep(1)
