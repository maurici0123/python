existe = False
materias = []
medias = []
y = 0

nome = input('Nome do aluno(a): ')
print('-='*10)

while (existe == False):
    qtd_materia = int(input('Número de matérias: '))
    print('-='*10)

    if (qtd_materia <= 0):
        print(
            '\033[31mQuantidade de matérias inválida. Por favor, insira um valor acima de 0\033[m')
        print('-='*10)
        existe = False
    else:
        existe = True

for x in range(qtd_materia):
    y = 0
    materias.clear()
    while (y < 4):
        nota = float(input(f'Nota da {x+1}º matéria do {y+1}º bimestre: '))

        if (nota >= 0 and nota <= 10):
            y += 1
            materias.append(nota)
        else:
            print('\033[31minsira um valor entre 0 a 10\033[m')
            continue
    medias.append(sum(materias)/4)
    print('-='*17)

for i, nota in enumerate(medias):
    if (nota <= 3):
        print(f'O aluno {nome} está \033[31mreprovado\033[m na {i+1}º matéria')
        print(f'NOTA: {nota:.2f}')
    elif (nota < 7):
        print(f'O aluno {nome} está de \033[33mrecuperação\033[m na {i+1}º matéria')
        print(f'NOTA: {nota:.2f}')
    else:
        print(f'O aluno {nome} está \033[32maprovado\033[m na {i+1}º matéria')
        print(f'NOTA: {nota:.2f}')
    print('-='*15)
