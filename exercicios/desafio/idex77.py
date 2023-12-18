text=('correr','jogar','estudar','cadeira','basquete','lapis','calendario','garrafa')
vogais=('a','e','i','o','u')

for p in text:
    print(f'a palavra {p} tem as vogais: ', end='')
    for c in range(0, len(p)):
        for v in vogais:
            if p[c]==v:
                print(p[c], end=' ')
    print()

    