"""
Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

"""

s = float(input("Qual é o seu salário : "))

print(f"Você terá um aumento de 15% totalizando R$ {(s * 15 / 100)} de desconto")
print(f"O produto irá custar R$ {s + (s * 15 / 100)}")