mat=[[],[],[]]
par=0

for c in range(0,3):
    x = int(input(f'digite o numero da posição [0][{c}]: '))
    mat[0].append(x)
    if x%2==0:
        par+=x

for c in range(0,3):
    x = int(input(f'digite o numero da posição [1][{c}]: '))
    mat[1].append(x)
    if x%2==0:
        par+=x
    if c==0:
        maior=x
    else:
        if mat[1][c]>maior:
            mat[1][c]=maior

for c in range(0,3):
    x = int(input(f'digite o numero da posição [2][{c}]: '))
    mat[2].append(x)
    if x%2==0:
        par+=x

soma = mat[0][2]+mat[1][2]+mat[2][2]

print('='*20)
print(mat[0])
print(mat[1])
print(mat[2])

print('='*20)
print(f'a soma dos vlores pares são: {par}')
print(f'a soma da 3º coluna são: {soma}')
print(f'o maior valor da 2º linha é: {maior}')