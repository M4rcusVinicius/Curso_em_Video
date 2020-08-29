"""
Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

"""

p = float(input("Qual é o preço do produto : "))


print(f"Você terá um desconto de 5% totalizando R$ {(p * 5 / 100)} de desconto")
print(f"O produto irá custar R$ {p - (p * 5 / 100)}")