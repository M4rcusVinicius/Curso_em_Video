valor = int(input('Qual o valor da casa ? '))
salario = int(input('Qual o seu salário atualmente ? '))
tempo = int(input('Em quantos anos você pretende pagar o emprestimo ? '))

pst = round(valor / (tempo * 12))
print(f'\nVocê irá pagar R$ {pst},00 por mês\n')

prc = (salario*3)/10

if pst < prc:
    print('Parabens! Você conseguio o emprestimo.')
    print(pst)
else:
    print('O seu emprestimo foi negado,\n'
          'O valor da prestação é maior que 30% do'
          'seu salário')