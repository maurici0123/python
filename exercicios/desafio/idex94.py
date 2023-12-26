data=[]
mulher=[]
maior=[]
person=dict()
media=0

while True:
    person['nome']=input('nome: ')
    person['sexo']=input('sexo [M/F]: ').upper()
    person['idade']=int(input('idade: '))

    media+=person['idade']
    if person['sexo']=='F':
        mulher.append(person['nome'])

    data.append(person.copy())
    person.clear()
    option=input('quer continuar [S/N]: ').upper()
    if option=='N':
        media=media/len(data)
        for x in data:
            if x['idade']>=media:
                maior.append(x['nome'])
        break

print('-='*25)
print(f'foram registradas {len(data)}')
print(f'a média da idade é {media}')
print(f'as mulheres registradas é {mulher}')
print(f'as pessoaa com a idade acima da média é {maior}')
print('-='*25)