n=0
c=1
s=0
while n!=999:
    n=int(input('{}º numero: '.format(c)))

    if n!=999:
        c+=1
        s+=n

print('a soma dos {} numeros é {}'.format(c-1, s))