"""
Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

"""

print("\n" * 10 + "Progressão Aritmética")

q = 10
n = int(input("Digite o 1° número : "))
r = int(input("Digite a razão da PA : "))
s = n + ( r * q )

while q != 0 :

    while n != s :
        n = n + r
        print(f"Progressão = {n}")

    q = int(input("Você gostaria de ver mais quantos termos : "))
    s = n + ( r * q )

