# convertor em binario de modo manual

dec = int(input('digite um numero inteiro: '))

b=[]
while dec!=3 and dec!=2:
    b.append(dec%2)
    dec = dec // 2
if dec == 2:
    b.append(0)
    b.append(1)
else:
    b.append(1)
    b.append(1)

r=[]
x = len(b)-1
while x>=0:
    r.append(b[x])
    x-=1

print(r)