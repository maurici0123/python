def num(*num):
    for c in num:
        print(f'{c} ', end='')
    print()

def soma(x, y):
    print(x+y)

#-----------------------------------
soma(3, 5)

num(3, 6, 8, 1, 3, 9)
num(3, 8, 1)
num(7, 8)