"""
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

"""
from random import randint

n = (randint(-100, 100), randint(-100, 100),randint(-100, 100), randint(-100, 100), randint(-100, 100))
maior = n[0]
menor = n[0]

for c in n:
    print(c, end = " --> ")
    if menor > c:
        menor = c
    if maior < c:
        maior = c

print("Fim")

print(f"O maior numero sorteano --> {maior}")
print(f"O menor numero sorteano --> {menor}")
print(f"O maior numero sorteano --> {max(n)}")
print(f"O menor numero sorteano --> {min(n)}")