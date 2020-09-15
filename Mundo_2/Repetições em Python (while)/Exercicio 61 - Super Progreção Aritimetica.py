n = int(input('Digite o primeiro termo : '))
r = int(input('Digite a rasão da PA : '))
n1 = n
qtd = 10
qtd1 = 0
n2 = 1
while n2 != 0:
    while n + r * qtd != n1:
        n1 = n1 + r
        print(n1)
    qtd1 += qtd
    qtd = int(input('Quantos mais progreções você gostaria de saber : '))
    n2 = n1
    qtd += qtd1