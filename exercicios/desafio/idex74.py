import random

n1=random.randint(0, 50)
n2=random.randint(0, 50)
n3=random.randint(0, 50)
n4=random.randint(0, 50)
n5=random.randint(0, 50)
num=(n1, n2, n3, n4, n5)

print(num)
sort=sorted(num)
print(sort[0])
print(sort[len(sort)-1])