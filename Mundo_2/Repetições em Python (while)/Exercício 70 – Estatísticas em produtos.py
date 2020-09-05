total = totmil = menor = cont = 0
barato = ""
while True:
    produto = str(input('Nome do produto: '))
    preço = float(input('Prese: R$'))
    cont += 1
    total += preço
    if preço > 1000:
        totmil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    resp = ''
    while resp not in 'SN':
        resp = str(input('Quer continuar? (S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:--40}'.format(' FIM DO PROGRAMA '))
print(f'o total da compra foi R${total:.2f}')
print(f'Temos {totmil} produtos sustando mais de R$1000.00')
print(f'o produto mais barate foi {barato} que custa R${menor:.2f}')