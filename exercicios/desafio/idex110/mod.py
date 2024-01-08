def dobro(p, sit=True):
    do = p*2
    if sit:
        return moeda(do)
    else:
        return f'{do:.2f}'

def metade(p, sit=True):
    me = p/2
    if sit:
        return moeda(me)
    else:
        return f'{me:.2f}'

def aumento(p, au, sit=True):
    au = p+((p/100)*au)
    if sit:
        return moeda(au)
    else:
        return f'{au:.2f}'

def diminuição(p, di, sit=True):
    di = p-((p/100)*di)
    if sit:
        return moeda(di)
    else:
        return f'{di:.2f}'

def moeda(p):
    return f'R${p:.2f}'.replace('.', ',')


def resumo(p, au, di):
    print('~'*33)
    print(f'preço analisado: \t{moeda(p)}')
    print(f'dobro do preço: \t{dobro(p)}')
    print(f'metade do preço: \t{metade(p)}')
    print(f'{au}% de aumento: \t{aumento(p, au)}')
    print(f'{di}% de redução: \t{diminuição(p, di)}')
    print('~'*33)