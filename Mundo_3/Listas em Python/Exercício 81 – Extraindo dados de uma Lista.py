"""
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso,mostre:
A) Quantos números foram digitados. 
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.

"""

from random import randint

lista = []
b = []
continuar = ""

while continuar == "s":
    n = int(input("Digite um numero : "))
    lista.append(n)
    continuar = str(input("Você deseja continuar : ")).lower[0]

print(f"Você digitou {len(lista)} números")
b = []
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for c in range(10, 0, -1):
    b.append(lista[c])
    print(f"VAlor {lista[c]} adcionado")
print(f"Lista de valores em ordem decrescente {b}")
    