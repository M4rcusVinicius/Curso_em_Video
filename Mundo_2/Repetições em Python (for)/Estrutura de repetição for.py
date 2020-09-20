s = 0

print('Contando de 1 até 10 : ',  end='')
for n in range(1, 11):
    print(f'{n}, ', end='')
    s += n
print('')

print('Contando de 10 até 1 : ', end='')
for n in range(10, 0, -1):
    print(f'{n}, ', end='')
    s += n
print('')

print('Contando apenas numeros pares : ', end='')
for n in range(0, 10, 2):
    print(f'{n}, ', end='')
    s += n
print('')

print(f'Somatorio de todos os numeros é igual a {s}')
