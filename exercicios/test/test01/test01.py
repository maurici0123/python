existe = False
materias = []
y=0

nome = input('Nome do aluno(a): ')
print('-='*10)  

while (existe == False):   
    qtd_materia = int(input('Número de matérias: '))
    print('-='*10)  

    if(qtd_materia<=0):
        print('\033[31mQuantidade de matérias inválida. Por favor, insira um valor acima de 0\033[m')
        print('-='*10)  
        existe = False
    else:
        existe = True

for x in range(qtd_materia):
    y=0
    while (y<4):
        n = float(input(f'Nota da {x+1}º matéria do {y+1}º bimestre: '))

        if (n >= 0):
            y+=1
        else:
            print('\033[31minsira um valor acima ou igual a de 0\033[m')
            continue
    print('-='*17)  