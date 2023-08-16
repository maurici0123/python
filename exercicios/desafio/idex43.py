peso = float(input('qual o seu peso: '))
altura = float(input('qual o seu altura: '))

imc = peso/(altura **2)

if imc < 18.5:
    print('\nIMC: {:.2f}\no status do seu imc é abaixo do peso'.format(imc))
elif imc < 25:
    print('\nIMC: {:.2f}\no status do seu imc é peso ideal'.format(imc))
elif imc < 30:
    print('\nIMC: {:.2f}\no status do seu imc é sobrepeso'.format(imc))
elif imc < 40:
    print('\nIMC: {:.2f}\no status do seu imc é obesidade'.format(imc))
else:
    print('\nIMC: {:.2f}\no status do seu imc é obesidade mórbida'.format(imc))