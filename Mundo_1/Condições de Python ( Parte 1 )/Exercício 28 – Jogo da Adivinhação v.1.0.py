"""
Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

"""

from random import randint
from time import sleep

n = randint(1, 5)
print("\n\n\n\nPensando em um número ...")
sleep(2)

r = int(input("Tente adivinhar o numero :"))
sleep(2)

if n == r:
    print("\nParabens, você acertou !!!")

if n != r:
    print("Você errou :/")

print(f"\nO número sorteado foi {n}")