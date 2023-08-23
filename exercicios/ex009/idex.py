n=s=0
c=0
while True:
    n=int(input('{}º numero: '.format(c)))
    if n==999:
        break

    c+=1
    s+=n

print('a soma dos {} numeros é {}'.format(c-1, s))