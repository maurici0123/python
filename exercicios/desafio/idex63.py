print('-'*22)
print('sequencia de fibonacci')
print('-'*22)

n=int(input('primeiros numeros da sequencia: '))

x=0
y=1
print(x, end=' - ')
print(y, end=' - ')

c=0
while c<n-2:
    s=x+y
    print(s, end=' - ') 
    x=y
    y=s

    c+=1

print('END')