"""
Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

"""
import math

n = float(input("Digite um ângulo : "))
sen = math.sin(math.radians(n))
cos = math.cos(math.radians(n))
tag = math.tan(math.radians(n))

print(f"""
Seno     == {sen}
Cosseno  == {cos}
Tangente == {tag}
""")