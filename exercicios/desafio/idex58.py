import random
r =1
x=0
c=0
while r!=x:
    r = random.randint(1,5)
    print('\nvoce tem que adivinhar um numero de um a cinco')
    x = int(input('digite um numero de [1:5]: '))
    c+=1

    if r!=x:
        print('voce \033[31mERROU\033[m')
    else:
        print('voce \033[32mACERTOU\033[m')
    
print('\nvoce precisou de {} chances'.format(c))