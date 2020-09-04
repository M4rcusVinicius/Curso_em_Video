"""
Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

"""
print("\n"*20 + "Maior e menor valor")
n = p = 0
n = int(input("Digite um número : "))
p = str(input("Você gostaria de continuar : ")).lower().strip()
t = n
c = 1
maior = n
menor = n
while "n" not in p:
    n = int(input("Digite um número : "))
    p = str(input("Você gostaria de continuar : ")).lower().strip()
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    t += n
    c += 1

print("="*100)
print(f"A média entre os valores é {t / c}")
print(f"O maior valor é {maior}")
print(f"O menor valor é {menor}")

