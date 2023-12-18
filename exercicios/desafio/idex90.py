aluno=dict()

aluno['name']= input('nome: ')
aluno['media']= float(input('média: '))

print('-'*10)
print(f'{"nome:":<10} {aluno["name"]}')
print(f'{"média:":<10} {aluno["media"]}')

if aluno["media"] >= 7:
    print(f'{"situação:":<10}\033[32m aprovado\033[m')
else:
    print(f'{"situação:":<10}\033[31m reprovado\033[m')

print('-'*10)