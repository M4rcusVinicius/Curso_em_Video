"""
Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:

considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

"""
valor = int(input("Digite o valor a ser sacado : "))

cinquenta = valor // 50
r = valor - cinquenta * 50

vinte = r // 20
r = r - vinte * 20

dez = r // 10
r = r - dez * 10

um = r // 1
r = r - um

print(f"Retirando {cinquenta} notas de R$ 50 ")
print(f"Retirando {vinte} notas de R$ 20 ")
print(f"Retirando {dez} notas de R$ 10")
print(f"Retirando {um} notas de R$ 1")
