import random

"""
Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

"""
print("\n" * 50)
c = 0
while True:
    print("=" * 50)
    escolha = input("Digite |P| para par e |I| para ímpar : ").lower().strip()
    n_jogador = int(input("Escolha um número : "))
    print("-" * 50)
    n_pc = random.randint(0, 11)
    soma = n_pc + n_jogador
    print(f"O computador escolheu o numero {n_pc}")
    print(f"A soma dos números é {soma}")
    if soma % 2 == 0:
        resultado = "p"
    else:
        resultado = "i"
    if resultado == escolha:
        print("\033[32mParabens! Você ganhou\033[m")
        c += 1
    else:
        print("\033[31mVocê perdeu!\033[m")
        print("=" * 50)
        break
    print("=" * 50)
    print("")
print(f"Você ganhou {c} vezes")