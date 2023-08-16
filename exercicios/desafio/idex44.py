valor = float(input('valor total da compra: '))

print('-'*32)
print('[1] á vista no dinheiro/cheque')
print('[2] á vista no cartão')
print('[3] em até 2x no cartão')
print('[4] 3x ou mais cartão')
print('-'*32)
option = int(input('opção: '))

if option == 1:
    print('\nvoce teve um desconte 10%\no valor ficou R${}'.format(valor*0.9))
elif option == 2:
    print('\nvoce teve um desconte 5%\no valor ficou R${}'.format(valor*0.95))
elif option == 3:
    print('\n voce vai pagar o valor normal\no valor ficou R${}'.format(valor))
elif option == 4:
    print('\nvoce teve um juros de 20%\no vlor ficou R${}'.format(valor*1.2))
else:
    print('as opçõe so vão de 1 a 4')