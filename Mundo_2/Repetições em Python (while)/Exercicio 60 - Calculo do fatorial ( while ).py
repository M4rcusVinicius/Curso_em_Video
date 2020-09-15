from time import sleep
print(f'{"=" * 4} Calculando o Fatorial {"=" * 4} ')
n = int(input('Digite um número : '))
print(f'{n}! = {n}', end='')
r = 0
n1 = n
while n1 != 1:
    n1 = n1 - 1
    r += n1
    print(f' . {n1}', end='')
    sleep(0.3)
print(f' = {r + n}')
