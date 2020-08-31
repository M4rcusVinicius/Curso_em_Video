"""
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

"""

r1 = int(input("Digite a 1° reta : "))
r2 = int(input("Digite a 2° reta : "))
r3 = int(input("Digite a 3° reta : "))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("O triângulo pode ser formado !!!")

else:
    print("O triângulo pode ser formado !!!")