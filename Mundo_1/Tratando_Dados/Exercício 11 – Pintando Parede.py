"""
Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

"""

l = float(input("Digite a largura da parede : "))
h = float(input("Digite altura da parede : "))

print(f"A area da parede é {l * h}")
print(f"Será preciso comprar {(l * h)/ 2}")
