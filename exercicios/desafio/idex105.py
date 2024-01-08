def nota(*n, situacao=False):
    l=len(n)

    maior=n[0]
    for c in n:
        if c>maior:
            maior=c

    menor=n[0]
    for c in n:
        if c<menor:
            menor=c

    media=sum(n)/l

    if situacao:
        if media>=7:
            sit='\033[32mboa\033[m'
        elif media>=5:
            sit='\033[33mrazuável\033[m'
        else:
            sit='\033[31mruim\033[m'
        return (f'quantidade de notas: {l}\nmaior nota: {maior}\nmenor nota: {menor}\na média da nota: {media:.2f}\nsituação: {sit}')
    else:
        return (f'quantidade de notas: {l}\nmaior nota: {maior}\nmenor nota: {menor}\na média da nota: {media:.2f}')

resp= nota(2, 4, 8, 6, 9, 5, situacao=True)
print('-='*15)
print(resp)
print('-='*15)