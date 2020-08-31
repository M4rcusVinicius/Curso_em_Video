"""
Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

"""

d = float(input("Digite a distancia da viagem em km : "))

if d <= 200:
    print(f"O preço da sua passagem será : R$ {d * 0.5}")

if d > 200:
    print(f"O preço da sua passagem será : R$ {d * 0.45}")
