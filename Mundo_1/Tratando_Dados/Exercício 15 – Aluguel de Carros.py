"""
Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

"""

km = float(input("Km percorridos pelo carro : "))
d = int(input("Quantidade de dias pelos quais o carro foi alugado : "))

print(f"O custo será R$ {(d * 60) + (km * 0.15)}")
