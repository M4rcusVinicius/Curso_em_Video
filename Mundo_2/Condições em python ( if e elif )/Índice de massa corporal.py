peso = float(input('informe o seu peso : '))
altura = float(input('informe a sua altura : '))

imc = peso / (altura ** 2)

print('O seu IMC é {:.1f}'.format(imc))

if imc < 18.5:
    print('Você está Abaixo do Peso')
elif imc < 25:
    print('Você está Peso Ideal')
elif imc < 30:
    print('Você está Sobrepeso')
elif imc < 40:
    print('Você está Obesidade')
else:
    print('Você está Obesidade Mórbida')