media=0
women=0
men=-1

for c in range(0, 4):
    name = input('nome: ')
    age = int(input('idade: '))
    gender = input('sexo [F/M]: ')
    gender.lower()
    print('-'*10)
    

    media+=age
    
    if gender=='m' and age>men:
        men=age
        old=name

    if gender=='f' and age<20:
        women +=1

print('a media da idade é {:.2f}'.format(media/4))
print('tem {} mulher(s) com menos de 20 anos'.format(women))
print('o homen mais velho é o {}'.format(old))