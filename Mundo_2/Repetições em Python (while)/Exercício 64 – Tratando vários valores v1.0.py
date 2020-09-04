"""
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

"""
n = t = c = 0

while n != 9:
    n = int(input("Digite um número [ 9 --> parar ]: "))
    if n != 9:
        t += n
        c += 1

print("="*100)
print(f"Você digitou {c} números totalizando {t}")
