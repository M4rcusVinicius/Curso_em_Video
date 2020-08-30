"""
Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

"""
import random

n1 = str(input("Digite o 1° nome : "))
n2 = str(input("Digite o 2° nome : "))
n3 = str(input("Digite o 3° nome : "))
n4 = str(input("Digite o 4° nome : "))

lista = [n1, n2, n3, n4]

print(f"O nome escolhido foi {random.choice(lista)}")
