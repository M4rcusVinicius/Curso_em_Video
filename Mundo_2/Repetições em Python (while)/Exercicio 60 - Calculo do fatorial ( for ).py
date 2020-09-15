print(f'\n{"=" * 4} Calculando o Fatorial {"=" * 4} ')
n = int(input("\nDigite um número : "))
print(f'{n}! = {n}', end='')

for c in range(n - 1, 0, -1):
    print(f' . {c}', end='')
print('')