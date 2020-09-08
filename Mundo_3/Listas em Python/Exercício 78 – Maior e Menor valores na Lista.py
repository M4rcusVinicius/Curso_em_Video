"""
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivos posições na lista.

"""
from random import randint
print("")

a = [randint(0, 50), randint(0, 50), randint(0, 50),
     randint(0, 50), randint(0, 50), ]

for c in range(0, len(a)):
    print(f"Valor {c+1} = {a[c]}")

print(f"\nO maior valor lido foi {max(a)} in position {a.index(max(a))+1}")
print(f"O menor valor lido foi {min(a)} in position {a.index(min(a))+1}")

