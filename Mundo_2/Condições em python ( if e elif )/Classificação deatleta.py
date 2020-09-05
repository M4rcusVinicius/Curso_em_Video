from datetime import date
hj = date.today().year

ano = int(input('Em que ano você nasceu ? '))
idade = hj - ano

if idade <= 9:
    print('Você é um atleta da classe mirim!')
elif 9 < idade <= 14:
    print('Você é um atleta da classe infantil!')
elif 14 < idade <= 19:
    print('Você é um atleta da classe Junior!')
elif 19 < idade <= 25:
    print('Você é um atleta da classe Sênior!')
elif 25 < idade:
    print('Você é um atleta da classe Master!')