def leiaDinheiro(msg):
    while True:
        p=(input(msg))
        p=p.replace(',', '.')

        if p.isalpha() or p.strip() == '':
            print(f'\033[31mERRO "{p}" é um preço inválido\033[m')
        else:
            p = float(p)
            return p
            break