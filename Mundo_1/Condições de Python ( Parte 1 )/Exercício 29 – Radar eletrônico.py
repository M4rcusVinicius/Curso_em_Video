"""
Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

"""

v = float(input("Qual a velocidade do carro : "))

if v <= 80:
    print("Bom dia !!!")

if v > 80:
    print("Multado, velocidade acima de 80 km/h")
    print(f"Valor da multa : R$ {(v - 80) * 7}")