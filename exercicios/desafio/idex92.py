import datetime

person=dict()

person['nome']=input('nome: ')
person['nascimento']= datetime.datetime.now().year-int(input('ano de nascimento: '))
person['ctps']=int(input('numero da CTPS (0 nao tem); '))

if person['ctps']==0:
    print('-'*15)
    print(f'nome : {person["nome"]}')
    print(f'idade : {person["nascimento"]}')
    print('-'*15)
else:
    person['salario']=float(input('qual é o seu salário: '))
    person['aposentadoria']=35+int(input('ano em que começou a trabalhar: '))

    print('-'*25)
    print(f'nome : {person["nome"]}')
    print(f'idade : {person["nascimento"]}')
    print(f'ano de aposentadoria : {person["aposentadoria"]}')
    print('-'*25)