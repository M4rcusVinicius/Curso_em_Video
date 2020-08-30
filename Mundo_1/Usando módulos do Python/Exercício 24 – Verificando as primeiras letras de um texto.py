"""
Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

"""

c = str(input("Digite o nome da sua cidade :")).strip()
print(c[:5].upper() == "SANTO")
