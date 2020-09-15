from time import sleep

e = 0
f = str(f'{"=" * 7} Calculadora {"=" * 7} ')
for c in range(0, 27):
    sleep(0.2)
    print(f[c:c+1], end='')
sleep(1)
print('')
n1 = int(input('\n\nDigite o primeiro número : '))
n2 = int(input('Digite o primeiro número : '))

while e != 6:
    e = int(input('\n\nPara calcular digite'
                  '\n|1| Soma'
                  '\n|2| multiplicar'
                  '\n|3| dividir'
                  '\n|4| maior número'
                  '\n|5| escolher novos números'
                  '\n|6| sair do programa'
                  '\nSua escolha : '))
    if e == 5:
        n1 = int(input('Digite o primeiro número : '))
        n2 = int(input('Digite o primeiro número : '))
    if e == 1:
        print(f'{n1} + {n2} = {n1 + n2}')
    if e == 2:
        print(f'{n1} x {n2} = {n1 * n2}')
    if e == 3:
        print(f'{n1} / {n2} = {n1 / n2}')
    if e == 4:
        if n1 > n2:
            print(f'O maior número é {n1}')
        elif n1 < n2:
            print(f'O maior número é {n2}')
        else:
            print(f'O dois números são iguais')

    if 5 < e < 1:
        print('Este número não é válido, para sair digite 5')

    f = str(f'{"=" * 7} Calculadora {"=" * 7} ')
print('\nDesligando a calculadora ')
for n in range(1, 27):
    sleep(0.3)
    print('.', end='')