from random import randint
from time import sleep

pessoa = 0
erro = 0
n = randint(1, 10)

dificuldade = input('Selecione a dificuldade do jogo \n'    
                    'Digite |F| para facil \n'                
                    'Digite |D| para dificil \n'              
                    'Sua resposta : ').strip().lower()[0]

print('Pensando em um número ...')

print(n)

if dificuldade == 'f':
    erro = -1
    while pessoa != n:
        pessoa = int(input('Qual número eu pensei : '))
        erro += 1
        if pessoa > n:
            print('\33[31mMenos!\33[m Tente mais uma vez')
        if pessoa < n:
            print('\33[31mMais!\33[m Tente mais uma vez')
        if pessoa == 8:
            erro = 'Fracasso'
            pessoa = n

    if erro == 0:
        print('\33[34mParabens!\33[m Você não errou nenhuma vez')
        print('Você está com 100% de sorte')
    elif erro == 'Fracasso':
        print('\33[31mErrado!\33[m Você foi capaz de errar todas as vezes')
        print('\33[31mParabens!\33[m Você Você está com 100% de azar')
    else:
        p = 100 - erro * 10
        print('\33[34mParabens!\33[m Você acertou')
        print(f'Você errou {erro} vezes')
        print(f'Você está com {p}% de sorte')

if dificuldade == 'd':
    pessoa = int(input('Qual número eu pensei : '))
    while pessoa != n:
        print('\33[31mErrado!\33[m Tente mais uma vez')
        pessoa = int(input('Qual número eu pensei : '))
        erro += 1
        if erro == 8:
            erro = 'Fracasso'
            pessoa = n

    if erro == 0:
        print('\33[34mParabens!\33[m Você não errou nenhuma vez')
        print('Você está com 100% de sorte')
    elif erro == 'Fracasso':
        print('\33[31mErrado!\33[m Você foi capaz de errar todas as vezes')
        print('\33[31mParabens!\33[m Você Você está com 100% de azar')
    else:
        p = 100 - erro * 10
        print('\33[34mParabens!\33[m Você acertou')
        print(f'Você errou {erro} vezes')
        print(f'Você está com {p}% de sorte')
