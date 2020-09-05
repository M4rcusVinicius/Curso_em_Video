c = t = 0

while True:
    n = int(input("Digite um número : "))
    if n == 999:
        break
    t += n
    c += 1
print(f"Você digitou {c} números")
print(f"A soma de todos os números é {t}")
