n = int(input('Digite o primeiro termo : '))
r = int(input('Digite a rasão da PA : '))
n1 = n

while n + r * 10 != n1:
    n1 = n1 + r
    print(n1)
