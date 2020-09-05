print('{:=^80}'.format(' MARCUS CONECTIONS '))
print('')

preço = float(input('Qual o valor da compra ? '))
print('Qual será a forma de pagamento :'
      '\n |1| À vista em dinheiro / cheque'
      '\n |2| À vista no cartão'
      '\n |3| Parcelado no cartão')
pago = int(input('Digite a sua opção : '))

if pago == 1:
    valor = preço * 0.90
    print(f'Sua compra de R$ {int(preço)},00 será paga a vista com 10% de desconto')
    juros = preço - valor
    print(f'O valor total será R$ {int(valor)},00 com R$ {int(juros)},00 de desconto')
elif pago == 2:
    valor = preço * 0.95
    print(f'Sua compra de R$ {int(preço)},00 será paga a vista com 5% de desconto')
    juros = preço - valor
    print(f'O valor total será R$ {int(valor)},00 com R$ {int(juros)},00 de desconto')
elif pago == 3:
    parcela = int(input('Você deseja parcelar em quentas vezes ? '))
    if parcela <= 0:
        print(f'Você é um imbecil, não é pocivel parcelar em {parcela} vezes')
    elif parcela == 1:
        print(f'Você é  um imbecil, parcelar em 1 vez é igual pagar a vista')
    elif parcela <= 2:
        valor = preço
        print(f'Sua compra de R$ {int(preço)},00 será parcelada em {parcela} vezes sem juros')
        print(f'O valor total será R$ {int(valor)},00')
    elif parcela > 2:
        valor = preço * 1.20
        juros = valor - preço
        mes = valor / parcela
        print(f'Sua compra de R$ {int(preço)},00 será parcelada em {parcela} vezes com 20 % de juros')
        print(f'O valor total será R$ {int(valor)},00 com R$ {int(juros)},00 de juros')
        print(f'Você irá pagar R$ {int(mes)},00 por mes')


