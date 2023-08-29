age=men=women=0

while True:
    g=input('sexo [F/M]: ').lower()
    a=int(input('idade: '))

    if a>18:
        age+=1
    if g=='m':
        men+=1
    if g=='f' and a<20:
        women+=1

    option=input('quer continuar [S/N]: ').lower()
    if option=='n':
        break

print('\ntem {} pessoas acima de 18 anoos'.format(age))
print(f'foram {men} homens cadastrados')
print(f'foram cadastradas {women} mulheres com menos de 20 anos')