"""
Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:
– O nome com todas as letras maiúsculas e minúsculas.
– Quantas letras ao todo (sem considerar espaços).
– Quantas letras tem o primeiro nome.

"""

n = str(input("Qual o seu nome : "))

print(f"Maiúsculas : {n.upper()}")
print(f"Minúsculas : {n.lower()}")
print(f"Quantidade de letras : {len(n.strip())}")
print(f"Quantidade de letras nome 1 : {len(n) - n.count(' ')}")
