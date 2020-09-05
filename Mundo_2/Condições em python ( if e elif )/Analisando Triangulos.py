l1 = float(input('  Infome o primeiro lado do triangulo em metros: '))
l2 = float(input('Informe o segundo lado do  triangulo em metros: '))
l3 = float(input('Informe o terceiro lado do triangulo em metros: '))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    if l1 == l2 == l3:
        print('Ok, suas medidas formam um triangulo EQUILATERO')
    elif l1 != l2 != l3 != l1:
        print('Ok, suas medidas formam um triangulo  ESCALENO.')

    else:
        print('Ok, suas medidas formam um triangulo ISOCELES.')
else:
    print("Suas medidas não formam um triangulo.")