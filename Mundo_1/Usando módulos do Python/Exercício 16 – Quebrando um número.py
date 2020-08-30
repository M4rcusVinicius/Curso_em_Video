"""
Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

"""
import math

n = float(input("Digite um número : "))

print(f"A parte inteira de {n} é {math.trunc(n)}")
print(f"A parte inteira de {n} é {int(n)}")
