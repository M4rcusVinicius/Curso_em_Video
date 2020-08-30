"""
O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

"""

import random

n1 = str(input("Digite o 1° nome : "))
n2 = str(input("Digite o 2° nome : "))
n3 = str(input("Digite o 3° nome : "))
n4 = str(input("Digite o 4° nome : "))
lista = [n1, n2, n3, n4]

random.shuffle(lista)

print(f" A sequencia escolhida foi : ")
print(lista)
