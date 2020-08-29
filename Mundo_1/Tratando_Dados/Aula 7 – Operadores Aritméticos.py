"""
  + ---> Mais
  - ---> Menos
  * ---> Multiplicação
  / ---> Divisão
 ** ---> Potência
 // ---> Divisão inteira
  % ---> Resto da Divisão

Ordem de precedência:
  1 ---> ()
  2 ---> **
  3 ---> *, /, //, %
  4 ---> +, -

"""
n1 = int(input("Digite um número : "))
n2 = int(input("Digite outro número : "))

print(f"{n1} +  {n2} == {n1 + n2}")
print(f"{n1} -  {n2} == {n1 - n2}")
print(f"{n1} *  {n2} == {n1 * n2}")
print(f"{n1} /  {n2} == {n1 / n2}")
print(f"{n1} ** {n2} == {n1 ** n2}")
print(f"{n1} // {n2} == {n1 // n2}")
print(f"{n1} %  {n2} == {n1 % n2}")

print("oi " * 10, "\n")

p1 = input("Digite uma Palavra : ")
print("")
print("Posicionamento | {:=<20} |".format(p1))
print("Posicionamento | {:=^20} |".format(p1))
print("Posicionamento | {:=>20} |\n".format(p1))
print(f"Posicionamento | {p1:20} |")
print(f"Posicionamento | {p1:^20} |")
print(f"Posicionamento | {p1:>20} |")