n = 'mau'
x = float(input('digite um numero: '))
y = float(input('digite outro numero: '))

a=x+y
s=x-y
m=x*y
d=x/y
di=x//y
p=x**y

print('\nola{:^10} \nadiçao {} \nsubtraçao {} \nmultiplicaçao {} \ndivisao {:.3f} \ndivisao inteira {} \npotenciaçao {}'.format(n, a, s, m, d, di, p))