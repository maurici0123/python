s = int(input('digite o numero inicial: '))
e = int(input('digite o numero final: '))

for c in range(s, e+1):
    if c%2 == 0:
        print(c,'é par')