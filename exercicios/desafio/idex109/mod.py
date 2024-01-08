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

def aumento(p, sit=True):
    au = p+(p/10)
    if sit:
        return moeda(au)
    else:
        return f'{au:.2f}'

def diminuição(p, sit=True):
    di = p-((p/100)*13)
    if sit:
        return moeda(di)
    else:
        return f'{di:.2f}'

def moeda(p):
    return f'{p:.2f}'.replace('.', ',')