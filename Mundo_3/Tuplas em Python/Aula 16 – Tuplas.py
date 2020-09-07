# Tuplas são imutaveis

lanche = ("Hambúrguer", "Suco", "Pizza", "Pudim")

print(lanche)
print(lanche[1])
print(lanche[2])
print(lanche[2:])
print(lanche[:3])
print(lanche[-1])

print(f"Você tem {len(lanche)} lanches")

for cont in range(0, len(lanche)):
    print(f"Eu vou comer {lanche[cont]} na posição {cont}")
print("Eu comi pra caramba !")

for pos, comida in enumerate(lanche):
    print(f"Eu vou comer {comida} na posição {pos}")
print("Eu comi pra caramba !")

for comida in lanche:
    print(f"Eu vou comer {comida}")
print("Eu comi pra caramba !")

print(sorted(lanche))