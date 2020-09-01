r = "Não"
r = str(input("Você gostaria de assinar a tim : ")).lower()

while r != "sim":
    r = str(input("\033[;31mVocê gostaria de assinar a tim : ")).lower()

print("\033[mMuito Obrigado ! Foi um prazer fazer negocios com você")
