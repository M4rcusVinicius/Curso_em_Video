"""
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

"""

n = str(input("Qual o seu nome : ")).strip().split()

print(f"Primeiro nome : {n[0]}")
print(f"Segundo nome  : {n[len(n)-1]}")


    
