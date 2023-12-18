mat=[[],[],[]]

for c in range(0,3):
    x = int(input(f'digite o numero da posição [0][{c}]: '))
    mat[0].append(x)

for c in range(0,3):
    x = int(input(f'digite o numero da posição [1][{c}]: '))
    mat[1].append(x)

for c in range(0,3):
    x = int(input(f'digite o numero da posição [2][{c}]: '))
    mat[2].append(x)

print('='*20)
print(mat[0])
print(mat[1])
print(mat[2])