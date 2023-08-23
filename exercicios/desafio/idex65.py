n=int(input('quantos numeros voce quer somar: '))

c=1
maior=menor=x=s=0

while c<=n:
    x=int(input('{}º: '.format(c)))

    if c==1:
        maior=menor=x
    else:
        if x>maior:
            maior=x
        if x<menor:
            menor=x

    s+=x
    c+=1

print('a media é {:.2f}'.format(s/n))
print('o maior numero é {}'.format(maior))
print('o menor numero é {}'.format(menor))