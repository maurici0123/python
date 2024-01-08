import datetime


def voto(idade):
    if idade<16:
        print(f'com {idade} anos voce não pode votar')
    if (idade>=16 and idade<18) or idade>=65:
        print(f'com {idade} anos o seu voto é opcional')
    if idade>=18 and idade<65:
        print(f'com {idade} anos o seu voto é obrigatório')


idade=datetime.datetime.now().year-int(input('em que ano voce nasceu: '))
voto(idade)