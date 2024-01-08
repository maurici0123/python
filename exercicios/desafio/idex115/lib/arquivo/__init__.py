from lib import interface

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    
def criarArquivo(nome):
    try:
        a = open(nome, 'w')
        a.close()
    except:
        print('houve um erro')
    else:
        print('arquivo criado com sucesso')

def lerArquivo(nome):
    try:
       a = open(nome, 'r', encoding='utf-8')
    except:
        print('\033[31m[ERRO]\033[m ao ler arquivo')
    else:
        interface.cabeçalho('PESSOAS REGISTRADAS')
        print(a.read())

def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'a', encoding='utf-8')
    except:
        print('houve um erro')
    else:
        try:
            a.write(f'\n{nome:<30}{idade:>3} anos')
        except:
            print('houve um erro em adicionar')
        else:
            print(f'novo registro de {nome} adicionado')
            a.close()