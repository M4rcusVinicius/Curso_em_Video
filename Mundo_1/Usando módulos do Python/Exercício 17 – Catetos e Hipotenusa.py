"""
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

"""
from math import hypot

o = float(input("Digite o cateto oposto : "))
a = float(input("Digite o cateto adjacente : "))
hp = hypot(o, a)

print(f"A hipotenusa é {(o ** 2 + a ** 2) ** (1/2)}")
print(f"A hipotenusa é {hp}")
