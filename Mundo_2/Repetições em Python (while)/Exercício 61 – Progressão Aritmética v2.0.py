"""
Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

"""

print("\n" * 10 + "Progressão Aritmética")

n = int(input("Digite o 1° número : "))
r = int(input("Digite a razão da PA : "))
s = n + ( r * 10 )

while n != s :
    n = n + r
    print(f"Progressão = {n}")

print("10 primeiros termos exibidos")

