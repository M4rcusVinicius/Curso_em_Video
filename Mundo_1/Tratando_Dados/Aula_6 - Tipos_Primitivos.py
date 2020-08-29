"""
int ---> números inteiros = 7, 3, 5
float ---> números reais = 7.09, 0.01 
bool ---> True ou False
str ---> Textos = "Alá", ""

"""

print("\n" * 30)

n1 = int(input("Digite um número : "))
n2 = input("Digite outro número : ")

print(type(n1))
print(type(n2))

s = int(n2) + n1

print("\n" + "A soma entre {} e {} é igual a {}".format(n1, n2, s))

try:
    print("\n" + "Other types : ")
    print("Str : " + str(n1))
    print("float : " + float(n1))
    print("bool : " + bool(n1))
    print("int : " + int(n1))
except:
    print("Other types are not supported")


    