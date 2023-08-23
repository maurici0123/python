print('-'*22)
print('progressão aritmética')
print('-'*22)
s = int(input('\nprimeiro termo: '))
p = int(input('razão: '))

for c in range(0, 10):
    print('{}'.format(s), end=' -> ')
    s+=p
print('end')

# end=''
# sep=''