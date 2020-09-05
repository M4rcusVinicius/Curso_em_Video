cont = 1

while True:
    n = int(input("Digite um número : "))
    if n == 999:
        break
    cont += n
print(f"A soma dos números é {cont}")