qtd = -1
soma = -999
n = 0
while n != 999:
    n = int(input("DIGITE UM NÚMERO : "))
    qtd += 1
    soma += n
print(f'Foram digitados {qtd} números, totalizando {soma}')