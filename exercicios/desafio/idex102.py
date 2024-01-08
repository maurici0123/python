def fatorial(x, show=False):
    f=1
    for c in range(1, x+1):
        f*=c

    if show:
        for c in range(1, x+1):
            print(f' {c} X', end='')
        print(f' = {f}')
    else:
        print(f'o fatorial de {x} é {f}')

        
fatorial(5, True)