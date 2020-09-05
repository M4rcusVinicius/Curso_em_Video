from random import randint
from time import sleep

op = int(input('''
Suas opções :
|1| Pedra
|2| Papel
|3| Tesoura\n
Sua escolha : '''))

if 0 < op < 4:
    sleep(1)
    print('\nJO', end='')
    sleep(1)
    print('KEM', end='')
    sleep(1)
    print('PO !\n')

    possivel = ('Pedra', 'Papel', 'Tesoura')
    pc = randint(0, 2)
    print(f'\nO computador escolheu {possivel[pc]}')

    if pc == 0:
        if op == 1:
            print('\033[33mImpapate')
        elif op == 2:
            print('\033[32mParabens! Você ganhou')
        elif op == 3:
            print('\033[31mVocê perdeu')
    if pc == 1:
        if op == 1:
            print('\033[31mVocê perdeu')
        elif op == 2:
            print('\033[33mImpapate')
        elif op == 3:
            print('\033[32mParabens! Você ganhou')
    if pc == 2:
        if op == 1:
            print('\033[32mParabens! Você ganhou')
        elif op == 2:
            print('\033[31mVocê perdeu')
        elif op == 3:
            print('\033[33mImpapate')

else:
    print('Você é um imbecil ?')
    print('Digite apenas 1, 2 ou 3')
