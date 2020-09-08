"""
Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

"""
from random import randint

lista = []

for contagem in range(0, 5):
    n = randint(0, 10)
    print(f"\nNumero sorteado == {n}")
    if contagem == 0:
        print("Primeiro numero adcionado")
        lista.append(n)
    else:
        c = 0
        if n > max(lista):
            print("Adionado na ultima posicao")
            lista.append(n)
        else:
            while n > lista[c]:
                c += 1
            lista.insert(c, n)
            print(f"Adcionado na posicao {c+1}")
        print(f"Lista = {lista}")