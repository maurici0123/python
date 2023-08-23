print('-'*22)
print('progressão aritmética')
print('-'*22)
s = int(input('\nprimeiro termo: '))
p = int(input('razão: '))

c=0
while c<10:
    print(s, '→ ', end='')
    s+=p
    c+=1

print('END')