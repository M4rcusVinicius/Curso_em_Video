"""
Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

"""

t = input("Aperte alguma tecla : ")

print("É um número         : ", t.isalnum())
print("É um número decimal : ", t.isdecimal())
print("É uma letra         : ", t.isalpha())
print("Está em maiúsculo   : ", t.isupper())
print("Está em minúsculo   : ", t.islower())
print("Está vazio          : ", t.isspace())
